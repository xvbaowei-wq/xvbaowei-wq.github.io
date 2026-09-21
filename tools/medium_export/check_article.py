#!/usr/bin/env python3
"""Check formula, image, and translation invariants for an article pair."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
IMAGE_RE = re.compile(r"^!\[[^]]*\]\(([^)]+)\)")


def parse(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[str] = []
    inline: list[str] = []
    images: list[str] = []
    headings: list[str] = []
    in_display = False
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == '<div class="math-display">':
            in_display = True
            current = []
            continue
        if in_display:
            if stripped == "</div>":
                blocks.append("\n".join(current).strip())
                in_display = False
            else:
                current.append(line)
            continue
        inline.extend(m.group(0) for m in INLINE_RE.finditer(line))
        image = IMAGE_RE.match(stripped)
        if image:
            images.append(image.group(1))
        if stripped.startswith("#"):
            headings.append(stripped)
    return {
        "lines": len(lines),
        "inline": inline,
        "blocks": blocks,
        "aligned": sum(r"\begin{aligned}" in b for b in blocks),
        "images": images,
        "headings": headings,
        "cjk_lines": [i for i, line in enumerate(lines, 1) if CJK_RE.search(line)],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("english", type=Path)
    args = parser.parse_args()
    source = parse(args.source)
    english = parse(args.english)

    # The English closing note intentionally repeats the final mirror-force
    # equation once; the original source formulas must still be an exact
    # ordered prefix of the English inline formulas.
    inline_prefix_ok = english["inline"][: len(source["inline"])] == source["inline"]
    block_diffs = []
    for index, (src, en) in enumerate(zip(source["blocks"], english["blocks"]), 1):
        normalized = en.replace(r"\text{net outward magnetic flux}", r"\text{净流出磁通}")
        normalized = normalized.replace(r"\text{volume}", r"\text{体积}")
        if src != normalized:
            block_diffs.append({"index": index, "source": src, "english": en})
    if len(source["blocks"]) != len(english["blocks"]):
        block_diffs.append({"reason": "block count mismatch"})

    important_tokens = [r"\mathbf", r"\hat", r"\boldsymbol", r"\partial", r"\nabla", r"\frac", r"\simeq", "O(r^3)", r"\begin{aligned}"]
    token_counts = {
        token: {"source": source_text.count(token), "english": english_text.count(token)}
        for token in important_tokens
        for source_text, english_text in [(args.source.read_text(encoding="utf-8"), args.english.read_text(encoding="utf-8"))]
    }
    report = {
        "source": str(args.source),
        "english": str(args.english),
        "source_inline_formula_count": len(source["inline"]),
        "english_inline_formula_count": len(english["inline"]),
        "english_extra_inline_formulas": english["inline"][len(source["inline"]):],
        "inline_formula_prefix_matches": inline_prefix_ok,
        "source_block_formula_count": len(source["blocks"]),
        "english_block_formula_count": len(english["blocks"]),
        "source_aligned_count": source["aligned"],
        "english_aligned_count": english["aligned"],
        "source_image_count": len(source["images"]),
        "english_image_count": len(english["images"]),
        "source_images": source["images"],
        "english_images": english["images"],
        "display_formula_diffs": block_diffs,
        "english_cjk_lines": english["cjk_lines"],
        "important_token_counts": token_counts,
        "passed": bool(
            inline_prefix_ok
            and not block_diffs
            and source["aligned"] == english["aligned"]
            and source["images"] == english["images"]
            and not english["cjk_lines"]
        ),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
