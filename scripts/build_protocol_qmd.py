#!/usr/bin/env python3
"""Build Protocol.qmd from the current SHARK-Seq website chapters.

The website contains HTML inputs, selects and textareas for interactive use.
This script replaces them with printable blanks in the PDF source so the
handout stays synchronized with the participant-facing workshop text.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

SOURCES = [
    "index.qmd",
    "01_reference_pcr.qmd",
    "02_edna_pcr.qmd",
    "primer_tools.qmd",
    "03_pcr_product_check.qmd",
    "04_pcr_cleanup.qmd",
    "05_quantification.qmd",
    "06_end_repair.qmd",
    "07_adapter_ligation.qmd",
    "08_flongle_loading.qmd",
    "09_minknow.qmd",
    "10_sequence_analysis.qmd",
    "workshop_decisions.qmd",
    "references.qmd",
]

PDF_HEADER = r'''---
title: "SHARK-Seq Workshop Protocol"
subtitle: "Reference-library and eDNA PCR workflow with Oxford Nanopore sequencing"
lang: en
format:
  pdf:
    pdf-engine: lualatex
    toc: true
    number-sections: false
    papersize: a4
    geometry:
      - top=18mm
      - bottom=18mm
      - left=18mm
      - right=18mm
    colorlinks: true
    linkcolor: blue
    urlcolor: blue
---
'''


def split_frontmatter(text: str):
    """Return (frontmatter, body)."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end < 0:
        return "", text
    return text[4:end], text[end + 5 :]


def title_from_frontmatter(front: str, fallback: str) -> str:
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', front, flags=re.M)
    return m.group(1).strip() if m else fallback


def printable_html(text: str) -> str:
    # For PDF, drop HTML-only alternatives and unwrap non-HTML alternatives.
    text = re.sub(r'::: \{\.content-visible when-format="html"\}\n.*?\n:::', '', text, flags=re.S)
    text = re.sub(r'::: \{\.content-visible unless-format="html"\}\n(.*?)\n:::', lambda m: m.group(1), text, flags=re.S)
    # Drop reset button entirely.
    text = re.sub(r'<button\b[^>]*>.*?</button>', '', text, flags=re.I | re.S)

    # Convert tool-button HTML anchors to ordinary Markdown links.
    text = re.sub(
        r'<a\s+href="([^"]+)"[^>]*>(?:<strong>)?(.*?)(?:</strong>)?</a>',
        lambda m: f'[{re.sub(r"<[^>]+>", "", m.group(2)).strip()}]({m.group(1)})',
        text,
        flags=re.I | re.S,
    )

    # Replace select blocks by a printable choice line.
    def repl_select(match):
        opts = re.findall(r'<option[^>]*>(.*?)</option>', match.group(0), flags=re.I | re.S)
        opts = [re.sub(r'<[^>]+>', '', o).strip() for o in opts]
        opts = [o for o in opts if o and not o.startswith('--')]
        suffix = f" ({' / '.join(opts)})" if opts else ""
        return f"______________________________{suffix}"

    text = re.sub(r'<select\b[^>]*>.*?</select>', repl_select, text, flags=re.I | re.S)

    # Replace input fields by printable blanks.
    text = re.sub(r'<input\b[^>]*>', '______________________________', text, flags=re.I)

    # Replace textareas by three writing lines.
    text = re.sub(
        r'<textarea\b[^>]*>.*?</textarea>',
        '\n\n________________________________________________________________________________\n\n________________________________________________________________________________\n\n________________________________________________________________________________\n',
        text,
        flags=re.I | re.S,
    )

    # Remove simple wrapper divs/remaining raw HTML tags.
    text = re.sub(r'</?div\b[^>]*>', '', text, flags=re.I)

    # Normalize checkbox glyphs in tables to ASCII-friendly symbols.
    text = text.replace('☐', '[ ]')

    # Ensure interactive-only classes are not required for PDF.
    return text.strip()


def build():
    parts = [PDF_HEADER.rstrip(), ""]

    for idx, rel in enumerate(SOURCES):
        path = ROOT / rel
        if not path.exists():
            raise FileNotFoundError(path)
        raw = path.read_text(encoding="utf-8")
        front, body = split_frontmatter(raw)
        title = title_from_frontmatter(front, path.stem.replace('_', ' ').title())
        body = printable_html(body)

        # index.qmd already has the document title in PDF YAML; include its body as intro.
        if rel == "index.qmd":
            parts.append(body)
            continue

        parts.extend(["", r"\newpage", "", f"# {title}", "", body])

    out = ROOT / "Protocol.qmd"
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
