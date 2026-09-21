#!/usr/bin/env python3
"""Prepare a Hugo article for Medium's URL import and audit the risks.

This does not claim that Medium renders LaTeX.  It removes Hugo-only wrappers,
turns page-bundle image paths into absolute URLs, and emits a manifest that
records the canonical URL and equation counts.  The source Hugo article
remains the canonical, fully typeset version.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urljoin


INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)")
BLOCK_RE = re.compile(r'<div class="math-display">\s*\n(.*?)\n</div>', re.S)
IMAGE_RE = re.compile(r"(!\[[^]]*\]\()([^)]+)(\))")


def read_base_url(repo_root: Path) -> str:
    config = (repo_root / "hugo.yaml").read_text(encoding="utf-8")
    match = re.search(r'^baseURL:\s*["\']?([^"\'\n]+)', config, re.M)
    if not match:
        raise ValueError("baseURL was not found in hugo.yaml")
    return match.group(1).strip().rstrip("/") + "/"


def canonical_url(repo_root: Path, source: Path, base_url: str) -> str:
    relative = source.resolve().relative_to(repo_root.resolve())
    parts = list(relative.parts)
    if parts and parts[0] == "content":
        parts = parts[1:]
    if parts[-1].startswith("index."):
        lang_suffix = parts[-1][len("index") : -len(".md")]
        parts = parts[:-1]
        if lang_suffix == ".en":
            parts = ["en", *parts]
    else:
        parts[-1] = parts[-1].removesuffix(".md")
    return urljoin(base_url, "/".join(parts).strip("/") + "/")


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML front matter")
    return text[end + len("\n---\n") :]


def prepare(repo_root: Path, source: Path, output: Path, canonical: str) -> dict:
    source_text = source.read_text(encoding="utf-8")
    body = strip_front_matter(source_text)
    body = body.replace('<div class="math-display">\n', "").replace('\n</div>', "")

    def image_rewrite(match: re.Match[str]) -> str:
        image_path = match.group(2)
        if image_path.startswith(("http://", "https://", "data:")):
            return match.group(0)
        return match.group(1) + urljoin(canonical, image_path) + match.group(3)

    body = IMAGE_RE.sub(image_rewrite, body)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(body, encoding="utf-8")

    blocks = BLOCK_RE.findall(source_text)
    inline = INLINE_RE.findall(source_text)
    manifest = {
        "source": str(source),
        "canonical_url": canonical,
        "medium_import_url": "https://medium.com/p/import",
        "inline_formula_count": len(inline),
        "block_formula_count": len(blocks),
        "aligned_count": sum(r"\begin{aligned}" in block for block in blocks),
        "image_count": len(IMAGE_RE.findall(source_text)),
        "formula_policy": "LaTeX delimiters are preserved for audit; Medium rendering must be checked in the live Draft.",
        "warnings": [
            "Do not treat a successful URL import as proof that $...$, $$...$$, or aligned formulas rendered.",
            "The Hugo page is the canonical source; this file is only a Medium import payload.",
        ],
    }
    manifest_path = output.with_suffix(".json")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--base-url")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    source = args.source.resolve()
    base_url = (args.base_url or read_base_url(repo_root)).rstrip("/") + "/"
    canonical = canonical_url(repo_root, source, base_url)
    output = args.output or repo_root / ".medium-export" / (source.parent.name + ".medium.md")
    manifest = prepare(repo_root, source, output, canonical)
    print(json.dumps({"output": str(output), "manifest": str(output.with_suffix('.json')), **manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
