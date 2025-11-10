#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import difflib
import os
import re
import sys
from typing import List, Tuple, Dict, Optional

FM_DELIM = "---"


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def extract_frontmatter(text: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FM_DELIM:
        return None, None, None
    # find closing delimiter
    for i in range(1, len(lines)):
        if lines[i].strip() == FM_DELIM:
            fm_lines = lines[1:i]
            fm = "\n".join(fm_lines) + "\n"
            body = "\n".join(lines[i+1:])
            return FM_DELIM + "\n" + fm + FM_DELIM + "\n", fm, body
    return None, None, None


def parse_kv_lines(fm_body: str) -> List[Tuple[str, str]]:
    # Very simple YAML-like key: value parser for single-line scalars (no lists, no nested)
    pairs: List[Tuple[str, str]] = []
    for raw in fm_body.splitlines():
        line = raw.rstrip("\r")
        if not line.strip():
            # skip empty spacing lines inside FM
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if not m:
            # keep unknown formatting line as passthrough with special key marker
            pairs.append(("__RAW__", raw))
            continue
        key = m.group(1)
        val = m.group(2)
        pairs.append((key, val))
    return pairs


def fm_pairs_to_text(pairs: List[Tuple[str, str]]) -> str:
    lines = []
    for k, v in pairs:
        if k == "__RAW__":
            lines.append(v)
        else:
            # keep value as-is, including empty
            lines.append(f"{k}: {v}" if v != "" else f"{k}:")
    return "\n".join(lines) + ("\n" if pairs else "")


def load_template_order(template_path: str) -> Tuple[List[str], Dict[str, str]]:
    t_text = read_file(template_path)
    full, fm, _ = extract_frontmatter(t_text)
    if not fm:
        raise RuntimeError(f"Template missing frontmatter: {template_path}")
    pairs = parse_kv_lines(fm)
    order: List[str] = []
    defaults: Dict[str, str] = {}
    for k, v in pairs:
        if k == "__RAW__":
            # ignore raw lines in template
            continue
        order.append(k)
        defaults[k] = v
    return order, defaults


def normalize_bool_str(v: str) -> str:
    lv = v.strip().lower()
    if lv in ["true", "false"]:
        return lv
    return v


def rebuild_frontmatter(existing_pairs: List[Tuple[str, str]],
                        canonical_order: List[str],
                        defaults: Dict[str, str]) -> List[Tuple[str, str]]:
    # map existing
    existing_map: Dict[str, str] = {}
    existing_extra: List[Tuple[str, str]] = []
    for k, v in existing_pairs:
        if k == "__RAW__":
            # preserve raw lines as extras at the end
            existing_extra.append((k, v))
            continue
        existing_map[k] = v
        if k not in canonical_order:
            existing_extra.append((k, v))

    rebuilt: List[Tuple[str, str]] = []
    for k in canonical_order:
        if k in existing_map:
            val = existing_map[k]
        else:
            val = defaults.get(k, "")
        # normalize booleans for toc/toc_sticky to be false if empty
        if k in ("toc", "toc_sticky"):
            if val.strip() == "":
                val = "false"
            val = normalize_bool_str(val)
        rebuilt.append((k, val))

    # append extras preserving their original order
    for k, v in existing_extra:
        if k != "__RAW__" and k in canonical_order:
            continue
        rebuilt.append((k, v))

    return rebuilt


def diff_text(a: str, b: str, fromfile: str, tofile: str) -> str:
    return "".join(
        difflib.unified_diff(
            a.splitlines(keepends=True),
            b.splitlines(keepends=True),
            fromfile=fromfile,
            tofile=tofile,
            lineterm="",
        )
    )


def check_and_optionally_fix(path: str, canonical_order: List[str], defaults: Dict[str, str], apply: bool, assume_yes: bool, dry_run: bool) -> bool:
    text = read_file(path)
    full, fm, body = extract_frontmatter(text)
    if full is None:
        print(f"[WARN] No frontmatter: {path}")
        return False

    orig_pairs = parse_kv_lines(fm)

    fixed_pairs = rebuild_frontmatter(orig_pairs, canonical_order, defaults)
    orig_text = FM_DELIM + "\n" + fm + FM_DELIM + "\n"
    fixed_fm_body = fm_pairs_to_text(fixed_pairs)
    fixed_text = FM_DELIM + "\n" + fixed_fm_body + FM_DELIM + "\n"

    if orig_text == fixed_text:
        print(f"[OK] {path}")
        return False

    d = diff_text(orig_text, fixed_text, fromfile=f"orig:{os.path.basename(path)}", tofile=f"fixed:{os.path.basename(path)}")
    print(f"[DIFF] {os.path.basename(path)}\n{d}\n")

    if dry_run:
        return True

    do_apply = apply
    if not do_apply:
        if assume_yes:
            do_apply = True
        else:
            try:
                ans = input("Appliquer ? [Entrée = non, y = oui, a = oui pour tous] ").strip().lower()
            except KeyboardInterrupt:
                print("\n(Interruption utilisateur)")
                return True
            do_apply = ans in ("y", "yes", "a", "all")

    if do_apply:
        new_content = fixed_text + (body or "")
        write_file(path, new_content)
        print(f"[APPLIED] {path}")
    else:
        print(f"[SKIPPED] {path}")

    return True


def find_md_files(root: str) -> List[str]:
    md_files: List[str] = []
    for entry in sorted(os.listdir(root)):
        if entry.lower().endswith(".md"):
            md_files.append(os.path.join(root, entry))
    return md_files

def project_canonical_keys_order(pairs: List[Tuple[str, str]], canonical_order: List[str]) -> List[str]:
    keys_in_order: List[str] = []
    for k, _ in pairs:
        if k == "__RAW__":
            continue
        if k in canonical_order:
            keys_in_order.append(k)
    return keys_in_order

def analyze_field_status(pairs: List[Tuple[str, str]], canonical_order: List[str], defaults: Dict[str, str], field: str) -> Tuple[str, Optional[int]]:
    # returns (status, current_index_in_projection or None)
    projection = project_canonical_keys_order(pairs, canonical_order)
    try:
        idx = projection.index(field)
    except ValueError:
        return ("missing", None)
    desired = canonical_order.index(field)
    if idx == desired:
        return ("ok", idx)
    return ("misplaced", idx)

def apply_rebuild_for_field(text: str, canonical_order: List[str], defaults: Dict[str, str]) -> str:
    full, fm, body = extract_frontmatter(text)
    if full is None:
        return text
    orig_pairs = parse_kv_lines(fm)
    fixed_pairs = rebuild_frontmatter(orig_pairs, canonical_order, defaults)
    fixed_fm_body = fm_pairs_to_text(fixed_pairs)
    fixed_text = FM_DELIM + "\n" + fixed_fm_body + FM_DELIM + "\n" + (body or "")
    return fixed_text

def create_frontmatter_from_template(existing_text: str, canonical_order: List[str], defaults: Dict[str, str]) -> str:
    # Build FM strictly in canonical order with defaults
    pairs: List[Tuple[str, str]] = []
    for k in canonical_order:
        v = defaults.get(k, "")
        if k in ("toc", "toc_sticky") and (v.strip() == ""):
            v = "false"
        pairs.append((k, v))
    fm_body = fm_pairs_to_text(pairs)
    return FM_DELIM + "\n" + fm_body + FM_DELIM + "\n" + (existing_text or "")


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Check and fix Constat frontmatter against template order.")
    parser.add_argument("--constats-dir", default=os.path.join("..", "..", "Public", "Constats"), help="Directory containing Constat Markdown files")
    parser.add_argument("--template", default=os.path.join("..", "..", "Éléments méthodologiques", "Templates", "Template Constat.md"), help="Path to template markdown file")
    parser.add_argument("--apply", action="store_true", help="Apply fixes without prompting")
    parser.add_argument("--yes", action="store_true", help="Assume 'yes' when prompting to apply per-file")
    parser.add_argument("--dry-run", action="store_true", help="Only show diffs; do not modify files")
    parser.add_argument("--diff", action="store_true", help="Use unified diff mode instead of step-by-field")

    args = parser.parse_args(argv)

    template_path = args.template
    constats_dir = args.constats_dir

    # Resolve relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.abspath(os.path.join(script_dir, template_path))
    constats_dir = os.path.abspath(os.path.join(script_dir, constats_dir))

    if not os.path.isfile(template_path):
        print(f"[ERROR] Template not found: {template_path}", file=sys.stderr)
        return 2
    if not os.path.isdir(constats_dir):
        print(f"[ERROR] Constats directory not found: {constats_dir}", file=sys.stderr)
        return 2

    order, defaults = load_template_order(template_path)

    # Ensure toc and toc_sticky default to false if template left blank
    for k in ("toc", "toc_sticky"):
        if k in defaults and defaults[k].strip() == "":
            defaults[k] = "false"

    md_files = find_md_files(constats_dir)
    if not md_files:
        print(f"[INFO] No markdown files in {constats_dir}")
        return 0

    # Default: Step-by-field mode (no flags needed). Use --diff for unified diff mode.
    if not args.diff:
        overall_changes = False
        apply_all = False
        for field in order:
            print(f"\n=== Champ: {field} ===")
            report: List[Tuple[str, str]] = []
            file_texts: Dict[str, str] = {}
            for fpath in md_files:
                text = read_file(fpath)
                file_texts[fpath] = text
                full, fm, _ = extract_frontmatter(text)
                if full is None:
                    report.append((fpath, "no_frontmatter"))
                    continue
                pairs = parse_kv_lines(fm)
                status, _ = analyze_field_status(pairs, order, defaults, field)
                report.append((fpath, status))
            # Print concise report
            for fpath, status in report:
                basename = os.path.basename(fpath)
                if status == "ok":
                    print(f"[OK] {basename}")
                elif status == "misplaced":
                    print(f"[MOVE] {basename} -> repositionner '{field}'")
                elif status == "missing":
                    print(f"[CREATE] {basename} -> ajouter '{field}'")
                else:
                    print(f"[CREATE FM] {basename} -> créer le frontmatter depuis le template")

            if all(s in ("ok",) for _, s in report):
                print("Tout est correct pour ce champ.")
                continue

            # Prompt apply for this field
            do_apply = False
            if args.apply or args.yes or apply_all:
                do_apply = True
            else:
                try:
                    ans = input("Appliquer pour ce champ ? [Entrée = non, y = oui, a = oui pour tous] ").strip().lower()
                except KeyboardInterrupt:
                    print("\n(Interruption utilisateur) - arrêt propre.")
                    print("Done.")
                    return 1 if overall_changes else 0
                if ans in ("a", "all"):
                    apply_all = True
                    do_apply = True
                else:
                    do_apply = ans in ("y", "yes")

            if do_apply:
                for fpath, status in report:
                    if status == "no_frontmatter":
                        new_text = create_frontmatter_from_template(file_texts[fpath], order, defaults)
                        if new_text != file_texts[fpath]:
                            write_file(fpath, new_text)
                            print(f"[CREATED FRONTMATTER] {os.path.basename(fpath)}")
                            overall_changes = True
                            # also update in-memory text for subsequent fields
                            file_texts[fpath] = new_text
                    elif status in ("misplaced", "missing"):
                        new_text = apply_rebuild_for_field(file_texts[fpath], order, defaults)
                        if new_text != file_texts[fpath]:
                            write_file(fpath, new_text)
                            print(f"[APPLIED] {os.path.basename(fpath)}")
                            overall_changes = True
                            file_texts[fpath] = new_text
            else:
                print("(Aucune modification appliquée pour ce champ)")

        print("Done.")
        return 1 if overall_changes else 0

    # Unified diff mode (only when --diff)
    had_changes = False
    for f in md_files:
        changed = check_and_optionally_fix(
            f, order, defaults, apply=args.apply, assume_yes=args.yes, dry_run=args.dry_run
        )
        had_changes = had_changes or changed

    print("Done.")
    return 1 if had_changes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
