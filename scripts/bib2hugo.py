#!/usr/bin/env python3
"""
bib2hugo.py — Convert BibTeX entries to Hugo/Wowchemy publication pages.

Usage:
    python scripts/bib2hugo.py bib/papers.bib
    python scripts/bib2hugo.py bib/papers.bib --update    # overwrite existing
    python scripts/bib2hugo.py bib/papers.bib --dry-run   # preview only
    python scripts/bib2hugo.py bib/papers.bib --en-only   # skip zh mirror

For each BibTeX entry the script creates:
    content/en/publication/<citekey>/index.md
    content/zh/publication/<citekey>/index.md  (mirror; translate manually)

The BibTeX citekey becomes the folder name (slugified).  If a folder already
exists the entry is skipped unless --update is passed.

Wowchemy publication_types legend
    0  Uncategorized
    1  Conference paper
    2  Journal article
    3  Preprint / Working Paper
    4  Report
    5  Book
    6  Book section
    7  Thesis
    8  Patent

BibTeX fields recognized
    Standard : title, author, year, month, booktitle, journal, publisher,
               volume, number, pages, doi, url, abstract, keywords, note
    arXiv    : eprint, archivePrefix (or archiveprefix)
    Custom   : featured = {true}   → mark publication as featured
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Optional dependency — install bibtexparser automatically
# ---------------------------------------------------------------------------
try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    import subprocess
    print("[bib2hugo] bibtexparser not found — installing…")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bibtexparser"])
    import bibtexparser                               # type: ignore
    from bibtexparser.bparser import BibTexParser    # type: ignore
    from bibtexparser.customization import convert_to_unicode  # type: ignore

# ---------------------------------------------------------------------------
# Paths (relative to this script's parent directory = project root)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
SITE_ROOT  = SCRIPT_DIR.parent
EN_PUB     = SITE_ROOT / "content" / "en" / "publication"
ZH_PUB     = SITE_ROOT / "content" / "zh" / "publication"

# ---------------------------------------------------------------------------
# Configuration — edit here to customise for the site owner
# ---------------------------------------------------------------------------

# Any of these names found in the BibTeX author field will be written as
# "admin" so that Wowchemy links the entry to the site owner's profile.
ADMIN_NAMES: set[str] = {
    "Meng Li",
    "Li, Meng",
    "M. Li",
}

# BibTeX entry-type → Wowchemy publication_type integer
PUBTYPE_MAP: dict[str, str] = {
    "article":       "2",
    "inproceedings": "1",
    "conference":    "1",
    "proceedings":   "1",
    "techreport":    "4",
    "report":        "4",
    "book":          "5",
    "inbook":        "6",
    "incollection":  "6",
    "phdthesis":     "7",
    "mastersthesis": "7",
    "thesis":        "7",
    "patent":        "8",
    "unpublished":   "3",
    "misc":          "3",
    "online":        "3",
    "preprint":      "3",
}

# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Return a URL-safe lowercase slug."""
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text


def clean_latex(text: str) -> str:
    """Strip common LaTeX markup, returning plain Unicode text."""
    if not text:
        return ""
    # Protect escaped braces before general brace removal
    text = text.replace(r"\{", "\x00LBRACE\x00").replace(r"\}", "\x00RBRACE\x00")
    # Unwrap simple {…} groups (case protection etc.)
    for _ in range(5):
        text = re.sub(r"\{([^{}]*)\}", r"\1", text)
    text = text.replace("\x00LBRACE\x00", "{").replace("\x00RBRACE\x00", "}")
    # Common inline commands
    text = re.sub(r"\\textit\{([^}]*)\}",  r"*\1*",    text)
    text = re.sub(r"\\textbf\{([^}]*)\}",  r"**\1**",  text)
    text = re.sub(r"\\emph\{([^}]*)\}",    r"*\1*",    text)
    text = re.sub(r"\\text[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    # Remaining commands
    text = re.sub(r"\\[a-zA-Z]+\*?\s?",    "",         text)
    text = re.sub(r"[{}]",                  "",         text)
    text = re.sub(r"\s{2,}",               " ",         text)
    return text.strip()


def yaml_scalar(value: str) -> str:
    """
    Return a YAML-safe representation of *value*.
    Uses double-quoted style only when the value contains characters that
    would break bare YAML scalars.
    """
    if not value:
        return '""'
    # Characters that require quoting in a plain YAML scalar
    must_quote = re.search(r'[:#\[\]{}&*!,?|>\'"\\]', value) or \
                 value[0] in ("-", "?", "|", ">", "@", "`") or \
                 value.startswith(" ") or value.endswith(" ")
    if must_quote:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def yaml_block(value: str) -> str:
    """
    Return the abstract as a quoted scalar that can span multiple lines.
    Uses double-quoted style so special characters are safe.
    """
    if not value:
        return '""'
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'

# ---------------------------------------------------------------------------
# BibTeX field parsers
# ---------------------------------------------------------------------------

def parse_authors(raw: str) -> list[str]:
    """
    Split a BibTeX author field on ' and ' and normalise each name to
    'First Last' order, replacing the site owner with 'admin'.
    """
    authors: list[str] = []
    for part in re.split(r"\s+and\s+", raw, flags=re.IGNORECASE):
        part = clean_latex(part.strip())
        if not part:
            continue
        if "," in part:
            last, first = part.split(",", 1)
            name = f"{first.strip()} {last.strip()}"
        else:
            name = part
        authors.append("admin" if name in ADMIN_NAMES else name)
    return authors


def parse_date(entry: dict) -> str:
    """Return an ISO-8601 datetime string (e.g. '2024-06-01T00:00:00Z')."""
    year = entry.get("year", str(datetime.now().year)).strip()
    month_raw = entry.get("month", "1").strip().lower()
    month_map = {
        "jan": 1, "january": 1,   "feb": 2, "february": 2,
        "mar": 3, "march": 3,     "apr": 4, "april": 4,
        "may": 5,                  "jun": 6, "june": 6,
        "jul": 7, "july": 7,      "aug": 8, "august": 8,
        "sep": 9, "september": 9, "oct":10, "october": 10,
        "nov":11, "november": 11, "dec":12, "december": 12,
    }
    month = month_map.get(month_raw)
    if month is None:
        try:
            month = int(month_raw)
        except ValueError:
            month = 1
    return f"{year}-{month:02d}-01T00:00:00Z"


def parse_venue(entry: dict) -> tuple[str, str]:
    """
    Return (publication, publication_short) strings.
    Conferences use 'In *Full Name*' / 'In *Abbrev Year*'.
    Journals use '*Full Name*'.
    """
    etype = entry.get("ENTRYTYPE", "misc").lower()
    is_journal = etype == "article"

    venue_full  = clean_latex(entry.get("journal" if is_journal else "booktitle", ""))
    venue_short = clean_latex(entry.get("journal_short",
                              entry.get("booktitle_short",
                              entry.get("series", ""))))
    year = entry.get("year", "")

    if is_journal:
        pub       = f"*{venue_full}*"  if venue_full  else ""
        pub_short = f"*{venue_short}*" if venue_short else pub
    else:
        prefix    = "In " if venue_full else ""
        pub       = f"{prefix}*{venue_full}*"  if venue_full  else ""
        short_str = venue_short or venue_full
        pub_short = (f"In *{short_str} {year}*".strip("* ").join(["In *", "*"])
                     if short_str else pub)
        # Simpler fallback
        if short_str:
            pub_short = f"In *{short_str} {year}*" if year else f"In *{short_str}*"

    return pub, pub_short


def parse_urls(entry: dict) -> dict[str, str]:
    """Collect PDF and auxiliary URLs from the entry."""
    urls = {k: "" for k in
            ("url_pdf", "url_code", "url_dataset",
             "url_poster", "url_project", "url_slides",
             "url_source", "url_video")}

    raw_url = entry.get("url", "").strip()
    doi     = entry.get("doi", "").strip()
    eprint  = entry.get("eprint", "").strip()
    archive = entry.get("archiveprefix",
              entry.get("archivePrefix", "")).strip().lower()

    # arXiv — highest priority for preprints
    if eprint and archive == "arxiv":
        urls["url_pdf"]    = f"https://arxiv.org/pdf/{eprint}"
        urls["url_source"] = f"https://arxiv.org/abs/{eprint}"

    # DOI
    if doi:
        if not urls["url_pdf"]:
            urls["url_pdf"] = f"https://doi.org/{doi}"

    # Generic URL — use as pdf or source
    if raw_url:
        if raw_url.lower().endswith(".pdf") or "pdf" in raw_url.lower():
            if not urls["url_pdf"]:
                urls["url_pdf"] = raw_url
        else:
            if not urls["url_source"]:
                urls["url_source"] = raw_url

    return urls


# ---------------------------------------------------------------------------
# Frontmatter builder
# ---------------------------------------------------------------------------

def build_frontmatter(entry: dict) -> str:
    title   = clean_latex(entry.get("title", "Untitled"))
    authors = parse_authors(entry.get("author", ""))
    date    = parse_date(entry)
    doi     = entry.get("doi", "").strip()
    pub_type = PUBTYPE_MAP.get(entry.get("ENTRYTYPE", "misc").lower(), "1")
    pub, pub_short = parse_venue(entry)
    abstract = clean_latex(entry.get("abstract", ""))

    raw_kw = entry.get("keywords", entry.get("keyword", ""))
    tags = [t.strip() for t in re.split(r"[,;]", raw_kw) if t.strip()] if raw_kw else []

    featured = entry.get("featured", "").strip().lower() in ("true", "yes", "1")
    urls = parse_urls(entry)

    lines = [
        "---",
        f"title: {yaml_scalar(title)}",
        "",
        "# Authors",
        "# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here",
        "# and it will be replaced with their full name and linked to their profile.",
        "authors:",
    ]
    for a in authors:
        lines.append(f"- {a}")

    lines += [
        "",
        f"date: {yaml_scalar(date)}",
        f"doi: {yaml_scalar(doi)}",
        "",
        "# Schedule page publish date (NOT publication's date).",
        f"publishDate: {yaml_scalar(date)}",
        "",
        "# Publication type.",
        "# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;",
        "# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;",
        "# 7 = Thesis; 8 = Patent",
        f'publication_types: ["{pub_type}"]',
        "",
        "# Publication name and optional abbreviated publication name.",
        f"publication: {pub}",
        f"publication_short: {pub_short}",
        "",
        f"abstract: {yaml_block(abstract)}",
        "",
        "tags:",
    ]
    for t in tags:
        lines.append(f"- {yaml_scalar(t)}")

    lines += [
        "",
        f"featured: {'true' if featured else 'false'}",
        "",
    ]
    for key, val in urls.items():
        val_str = yaml_scalar(val) if val else "''"
        lines.append(f"{key}: {val_str}")

    lines += ["---", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry slug
# ---------------------------------------------------------------------------

def entry_slug(entry: dict) -> str:
    """Derive a folder name.  Prefer the BibTeX citekey; fall back to
    <venue>-<year>-<first-title-word>."""
    key = entry.get("ID", "").strip()
    if key:
        return slugify(key)
    etype  = entry.get("ENTRYTYPE", "misc").lower()
    venue  = entry.get("booktitle" if etype != "article" else "journal", "pub")
    year   = entry.get("year", "0000")
    word   = (entry.get("title", "untitled").split() + ["paper"])[0]
    return slugify(f"{venue}-{year}-{word}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Convert BibTeX entries to Hugo/Wowchemy publication pages."
    )
    ap.add_argument("bibfile",    help="Path to the .bib file")
    ap.add_argument("--update",   action="store_true",
                    help="Overwrite pages that already exist")
    ap.add_argument("--dry-run",  action="store_true",
                    help="Print what would be written without touching disk")
    ap.add_argument("--en-only",  action="store_true",
                    help="Only create content/en pages (skip zh mirror)")
    args = ap.parse_args()

    bib_path = Path(args.bibfile)
    if not bib_path.exists():
        sys.exit(f"[bib2hugo] File not found: {bib_path}")

    bib_parser = BibTexParser(common_strings=True)
    bib_parser.customization = convert_to_unicode
    with bib_path.open(encoding="utf-8") as fh:
        db = bibtexparser.load(fh, bib_parser)

    print(f"[bib2hugo] {bib_path}  →  {len(db.entries)} entr"
          f"{'y' if len(db.entries)==1 else 'ies'} found\n")

    counts = {"created": 0, "updated": 0, "skipped": 0}

    for entry in db.entries:
        slug     = entry_slug(entry)
        en_dir   = EN_PUB / slug
        zh_dir   = ZH_PUB / slug
        exists   = en_dir.exists()

        if exists and not args.update:
            print(f"  [skip]   {slug}  (use --update to overwrite)")
            counts["skipped"] += 1
            continue

        content = build_frontmatter(entry)

        if args.dry_run:
            sep = "─" * 64
            print(f"\n{sep}")
            print(f"  {'[update]' if exists else '[create]'}  {slug}/index.md")
            print(sep)
            print(content)
            counts["updated" if exists else "created"] += 1
            continue

        # Write English
        en_dir.mkdir(parents=True, exist_ok=True)
        (en_dir / "index.md").write_text(content, encoding="utf-8")

        # Write Chinese mirror (unless --en-only)
        if not args.en_only:
            zh_dir.mkdir(parents=True, exist_ok=True)
            (zh_dir / "index.md").write_text(content, encoding="utf-8")

        label = "updated" if exists else "created"
        zh_note = "" if args.en_only else " (+zh mirror)"
        print(f"  [{label}]  {slug}{zh_note}")
        counts[label] += 1

    total = sum(counts.values())
    print(f"\n[bib2hugo] Done — "
          f"{counts['created']} created, "
          f"{counts['updated']} updated, "
          f"{counts['skipped']} skipped  "
          f"(total {total})")


if __name__ == "__main__":
    main()
