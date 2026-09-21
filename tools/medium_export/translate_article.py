#!/usr/bin/env python3
"""Generate a faithful English Hugo page from a reviewed Chinese source.

The translation table contains prose only.  Inline math is copied from the
source line-by-line, and display-math blocks are copied verbatim (apart from
explicitly listed translations of visible ``\\text{...}`` labels).  This
prevents a translation pass from silently changing mathematical notation.

This is intentionally a deterministic tool: for a new article, add a
translation table keyed by source line number rather than relying on a
second, independently typed copy of the equations.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


# The values are prose-only templates.  ``⟦0⟧`` means “insert the first
# inline formula from the corresponding source line”, etc.
TRANSLATIONS: dict[int, str] = {
    12: "> This note starts from magnetic-flux conservation in cylindrical coordinates. It keeps the intermediate derivation as complete as possible and adds the necessary mathematical steps and conditions of validity where a shortcut would otherwise be easy to miss.",
    14: "## The problem",
    16: "How can a magnetic mirror produce a reflection force along a magnetic field line?",
    18: "We consider only the **static, non-relativistic case with no electric field**. The ⟦0⟧ direction is chosen to coincide with the dominant magnetic-field direction near the axis, so ⟦1⟧ in the region under consideration.",
    20: "The Lorentz force is",
    28: "Write the magnetic field in cylindrical coordinates as",
    36: "and Maxwell's equation gives",
    44: "We begin with a small cylindrical volume element.",
    46: "![Differential cylindrical volume element](fig-1-fixed.png)",
    48: "*Figure 1. A differential sector-shaped cylindrical volume element, showing ⟦0⟧, ⟦1⟧, and ⟦2⟧.*",
    50: "The ranges of the volume element are",
    60: "The corresponding differential lengths in the three directions are",
    68: "Therefore, the volume is approximately",
    76: "We now calculate the net outward magnetic flux through the six faces of this volume element.",
    78: "## The basic form of magnetic flux",
    80: "The differential magnetic flux is",
    88: "where ⟦0⟧ is the area of the surface element and ⟦1⟧ is the outward unit normal of that surface.",
    90: "## Magnetic flux through the two radial faces",
    92: "![Radial-face geometry](fig-2.webp)",
    94: "*Figure 2. Geometry and outward normal directions of the radial faces.*",
    96: "### Inner face at ⟦0⟧",
    98: "The area of this face is",
    106: "The outward normal of the inner face is ⟦0⟧, so",
    117: "Expand the magnetic field completely:",
    134: "Taking the dot product term by term:",
    146: "Because the three cylindrical-coordinate unit basis vectors are mutually orthogonal,",
    158: "Therefore,",
    166: "Hence,",
    178: "### Outer face at ⟦0⟧",
    180: "The area of this face is",
    190: "At ⟦0⟧, the magnetic field is",
    198: "The outward normal is ⟦0⟧, so",
    209: "Again, expand the dot product completely:",
    235: "Therefore,",
    247: "### Net outward flux through the two radial faces",
    259: "Substituting the fluxes through the two faces gives",
    273: "Define",
    281: "Then",
    291: "From the definition of the derivative,",
    302: "Because ⟦0⟧ is infinitesimal, we can write the first-order approximation",
    312: "Thus,",
    322: "Here ⟦0⟧ actually comes from the multivariable function ⟦1⟧. When varying ⟦2⟧, ⟦3⟧ are held fixed, so a partial derivative should be used:",
    332: "Therefore,",
    345: "## Magnetic flux through the two ⟦0⟧-direction faces",
    347: "![Theta-direction side faces](fig-3-fixed.png)",
    349: "*Figure 3. The ⟦0⟧-direction side faces and their outward normal directions.*",
    351: "We repeat the same projection procedure for the two ⟦0⟧-direction faces. Although the form is similar to that for the radial faces, writing it out explicitly makes each normal projection clear.",
    353: "### Inner face at ⟦0⟧",
    355: "The two edges of this face are ⟦0⟧ and ⟦1⟧, so",
    363: "The outward normal of this face is ⟦0⟧, therefore",
    374: "Expand the magnetic field:",
    391: "Taking the dot product term by term:",
    403: "Using",
    415: "we obtain",
    423: "Therefore,",
    435: "### Outer face at ⟦0⟧",
    437: "The other face is at ⟦0⟧, with outward normal ⟦1⟧:",
    448: "Expand the dot product:",
    475: "Thus,",
    487: "### Net outward flux through the two ⟦0⟧ faces",
    499: "Therefore,",
    513: "As before, hold the other variables fixed and consider only the variation in ⟦0⟧:",
    523: "Therefore,",
    536: "## Magnetic flux through the two ⟦0⟧-direction faces",
    538: "![Upper and lower faces with outward normals](fig-4.webp)",
    540: "*Figure 4. The upper and lower ⟦0⟧-faces and their outward normal directions.*",
    542: "### Lower face at ⟦0⟧",
    544: "The two edges of the lower face are ⟦0⟧ and ⟦1⟧, so",
    554: "The outward normal of the lower face is ⟦0⟧, therefore",
    565: "Expand the dot product:",
    582: "That is,",
    594: "Since",
    606: "we have",
    614: "Therefore,",
    626: "### Upper face at ⟦0⟧",
    628: "The outward normal of the upper face is ⟦0⟧:",
    639: "Expand the dot product:",
    665: "Therefore,",
    677: "### Net outward flux through the two ⟦0⟧ faces",
    689: "Thus,",
    704: "Using the same finite-difference approximation as above,",
    714: "Therefore,",
    727: "## Obtaining the cylindrical-coordinate divergence from the fluxes in the three directions",
    729: "The total net outward magnetic flux through the six faces is",
    739: "Substituting the results from the three directions gives",
    758: "Factor out the common differential-volume factor:",
    775: "The divergence is defined as",
    786: "For the present differential volume element,",
    794: "Therefore,",
    804: "Substitute both ⟦0⟧ and ⟦1⟧:",
    825: "Cancel the common factor ⟦0⟧:",
    844: "which is the familiar form",
    860: "## Using the axisymmetry of the magnetic mirror",
    862: "The magnetic mirror is invariant under rotation about the ⟦0⟧ axis, so physical quantities do not depend on ⟦1⟧. Hence,",
    870: "In addition, we assume here that there is no azimuthal magnetic field:",
    878: "These two conditions must be distinguished: axisymmetry gives a zero partial derivative with respect to ⟦0⟧, whereas ⟦1⟧ is an additional assumption about the magnetic-field structure.",
    880: "Thus,",
    892: "Maxwell's equation also requires",
    900: "Therefore,",
    913: "## Using ⟦0⟧ to obtain ⟦1⟧ near the axis",
    915: "From the equation above,",
    925: "that is,",
    935: "![Magnetic mirror field lines](fig-5.webp)",
    937: "*Figure 5. Magnetic field lines near the axis of a magnetic mirror; the red line marks a reference line close to the axis.*",
    939: "Near the axis, if ⟦0⟧ varies sufficiently slowly in space, then in the present lowest-order approximation ⟦1⟧ can be treated as approximately constant with respect to ⟦2⟧.",
    941: "More precisely, what is required here is that **near the axis, at fixed ⟦0⟧, the variation of ⟦1⟧ with ⟦2⟧ can be neglected at the order being retained.** Under axisymmetry, near the axis we can write",
    949: "Therefore,",
    961: "At the lowest retained order, ⟦0⟧ can be taken outside the integral with respect to ⟦1⟧.",
    963: "To avoid confusing the integration variable with the upper limit, write the ⟦0⟧ inside the integral as ⟦1⟧:",
    975: "The left-hand side integrates directly:",
    986: "On the axis, ⟦0⟧; provided ⟦1⟧ remains finite, we have",
    994: "The right-hand side is",
    1006: "Therefore,",
    1017: "We finally obtain",
    1030: "More rigorously, this is the lowest-order result near the axis:",
    1042: "If moving in the ⟦0⟧ direction, ⟦1⟧ slowly increases,",
    1050: "then",
    1058: "That is, the radial magnetic-field component points in the ⟦0⟧ direction.",
    1060: "## Obtaining a force in the ⟦0⟧ direction from the radial magnetic field",
    1062: "The particle is also undergoing gyromotion; denote its azimuthal velocity by ⟦0⟧.",
    1064: "The Lorentz force remains",
    1072: "Under the present axisymmetric, ⟦0⟧ condition,",
    1080: "Write the velocity as",
    1094: "We consider only the ⟦0⟧ component of the Lorentz force. The term in the cross product that can produce a ⟦1⟧ component is",
    1104: "Because",
    1114: "we have",
    1124: "Hence,",
    1134: "Substituting",
    1145: "gives",
    1156: "### Relating ⟦0⟧ to the Larmor radius",
    1158: "We next use",
    1168: "To connect this directly to the ⟦0⟧ in the preceding equation, first consider a **special orbit whose guiding center lies exactly on the axis**. In this near-axis local model, the particle's gyro-orbit is centered on the axis, so the particle's distance from the axis is the Larmor radius,",
    1176: "and",
    1184: "This signed Larmor relation can also be obtained directly from the radial Lorentz force.",
    1186: "Locally approximate the magnetic field as",
    1194: "The circular motion of the particle requires the centripetal acceleration",
    1202: "The radial Lorentz force is",
    1212: "Thus,",
    1222: "When ⟦0⟧,",
    1232: "Because the magnitude of the gyromotion velocity is ⟦0⟧,",
    1240: "we have",
    1252: "Substitute this back into ⟦0⟧:",
    1269: "Define the magnetic moment",
    1279: "Then",
    1290: "### Rewriting the ⟦0⟧-direction result as a force along the magnetic field",
    1292: "Starting from the near-axis result",
    1301: "we write it as",
    1309: "and then as",
    1317: "Two approximations are implicit in these steps and should be stated explicitly.",
    1319: "First, near the axis the radial component ⟦0⟧ is small and the magnetic field is mainly in the ⟦1⟧ direction, so",
    1333: "Thus, at the current lowest order,",
    1343: "Therefore,",
    1353: "Second, define the gradient along the magnetic field line by",
    1367: "Near the axis,",
    1375: "so",
    1385: "At the same time, the ⟦0⟧ direction is approximately the magnetic-field-line direction, so",
    1393: "Combining these results, under the near-axis and slowly varying-field approximations for the magnetic mirror,",
    1405: "This is the standard magnetic mirror-force form. The explicit calculation above treats the near-axis special case in which the guiding center lies on the axis; for a general guiding-center position, the fast gyro-phase must be averaged. First-order guiding-center theory gives the same standard result ⟦0⟧.",
    1407: "### What conditions of validity are implicit in this derivation?",
    1409: "Using local Larmor gyromotion and the magnetic moment ⟦0⟧ also assumes that the magnetic field varies slowly over one Larmor-radius scale; typically,",
    1417: "where ⟦0⟧ is the spatial scale over which the magnetic field changes significantly.",
    1419: "Under this adiabatic condition, the particle gyros rapidly while the guiding center experiences a slowly varying magnetic field, and the magnetic moment",
    1427: "can be used as an invariant at first adiabatic order in the non-relativistic approximation.",
    1429: "## Conclusion",
    1431: "The logic of the derivation can be summarized as follows:",
    1433: "1. Start from ⟦0⟧;",
    1434: "2. Compute the magnetic flux through each face of a differential cylindrical volume element and derive the divergence formula;",
    1435: "3. For an axisymmetric magnetic mirror with no azimuthal magnetic field, obtain near the axis",
    1446: "4. The particle's gyromotion velocity ⟦0⟧ couples to the small radial magnetic field ⟦1⟧ through the Lorentz force and produces a force in the ⟦2⟧ direction;",
    1447: "5. Under the guiding-center and adiabatic approximations, average over the fast gyromotion to obtain the standard magnetic mirror force",
    1457: "Therefore, the “reflection force along the magnetic field line” in a magnetic mirror is not a new fundamental force applied directly along the field line. It is an effective parallel force that emerges on the guiding-center scale from the combined action of the nonuniform magnetic field, gyromotion, and ⟦0⟧.",
}


# Visible text inside a copied display formula must also be translated.  No
# symbolic part of any equation is changed by this mapping.
FORMULA_REWRITES = {
    r"\text{净流出磁通}": r"\text{net outward magnetic flux}",
    r"\text{体积}": r"\text{volume}",
}

INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def inline_formulas(line: str) -> list[str]:
    return [m.group(0) for m in INLINE_RE.finditer(line)]


def inject_inline_formulas(source_line: str, template: str) -> str:
    formulas = inline_formulas(source_line)
    placeholders = [f"⟦{i}⟧" for i in range(len(formulas))]
    if template.count("⟦") != len(formulas):
        raise ValueError(
            f"inline formula placeholder mismatch: source={source_line!r}, "
            f"template={template!r}, formulas={len(formulas)}"
        )
    result = template
    for marker, formula in zip(placeholders, formulas):
        result = result.replace(marker, formula, 1)
    return result


def generate(source: Path, destination: Path) -> None:
    source_lines = source.read_text(encoding="utf-8").splitlines()
    output: list[str] = [
        "---",
        'title: "From ∇·B = 0 to the Magnetic Mirror Force: A Complete Near-Axis Derivation"',
        "date: 2026-09-17T08:44:00+08:00",
        "draft: false",
        'description: "A complete near-axis derivation of the magnetic mirror force, starting from ∇·B = 0 in cylindrical coordinates."',
        'categories: ["Plasma Physics"]',
        'tags: ["magnetic mirror", "guiding-center theory"]',
        "math: true",
        "showToc: true",
        "lang: en",
        "---",
        "",
    ]
    in_math_display = False
    seen: set[int] = set()
    for line_number, source_line in enumerate(source_lines, 1):
        stripped = source_line.strip()
        if line_number <= 10:
            continue
        if stripped == '<div class="math-display">':
            in_math_display = True
            output.append(source_line)
            continue
        if in_math_display:
            rewritten = source_line
            for old, new in FORMULA_REWRITES.items():
                rewritten = rewritten.replace(old, new)
            output.append(rewritten)
            if stripped == "</div>":
                in_math_display = False
            continue
        if not stripped:
            output.append("")
            continue
        if line_number not in TRANSLATIONS:
            raise ValueError(f"missing translation for source line {line_number}: {source_line!r}")
        translated = inject_inline_formulas(source_line, TRANSLATIONS[line_number])
        if CJK_RE.search(translated):
            raise ValueError(f"untranslated CJK remains on source line {line_number}: {translated!r}")
        output.append(translated)
        seen.add(line_number)

    missing = sorted(set(TRANSLATIONS) - seen)
    if missing:
        raise ValueError(f"translation entries were not used: {missing}")

    output.extend(
        [
            "",
            "> This note is part of my ongoing study of plasma physics. Rather than simply memorizing $F_\\parallel=-\\mu\\nabla_\\parallel B$, I wanted to keep a complete record of where the result comes from and which approximations enter at each step.",
            ">",
            "> This article is maintained as part of my personal research notes: *Trajectories & Fields*.",
        ]
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or args.source.with_name("index.en.md")
    generate(args.source, output)
    print(output)


if __name__ == "__main__":
    main()
