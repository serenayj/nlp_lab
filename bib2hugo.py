#!/usr/bin/env python3
"""
BibTeX → HugoBlox publication converter
Usage: python bib2hugo.py my_papers.bib
Generates content/publication/<slug>/index.md for each entry.
"""

import re
import os
import sys
import argparse

def parse_bibtex(bib_text):
    """Simple BibTeX parser — handles most standard entries."""
    entries = []
    # Match each @TYPE{key, ...} block
    pattern = re.compile(r'@(\w+)\s*\{\s*([^,]+)\s*,\s*(.*?)\n\}', re.DOTALL | re.IGNORECASE)

    for m in pattern.finditer(bib_text):
        entry_type = m.group(1).lower()
        key = m.group(2).strip()
        body = m.group(3)

        fields = {}
        # Match field = {value} or field = "value" or field = number
        field_pat = re.compile(r'(\w+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|"([^"]*)"|([\d]+))', re.DOTALL)
        for fm in field_pat.finditer(body):
            fname = fm.group(1).lower()
            fval = fm.group(2) or fm.group(3) or fm.group(4) or ''
            # Clean up whitespace and nested braces
            fval = re.sub(r'\s+', ' ', fval).strip()
            fval = fval.replace('{', '').replace('}', '')
            fields[fname] = fval

        entries.append({'type': entry_type, 'key': key, 'fields': fields})

    return entries


def make_slug(key, title):
    """Generate a filesystem-safe slug from the BibTeX key."""
    slug = re.sub(r'[^a-z0-9\-]', '-', key.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


def pub_type(entry_type, fields):
    """Map BibTeX entry type to HugoBlox publication_types."""
    t = entry_type.lower()
    venue = (fields.get('booktitle', '') + fields.get('journal', '')).lower()
    if t in ('article',):
        return 'article-journal'
    elif t in ('inproceedings', 'proceedings', 'conference'):
        return 'paper-conference'
    elif t in ('techreport', 'misc') and 'arxiv' in venue:
        return 'article'  # preprint
    elif t in ('phdthesis', 'mastersthesis'):
        return 'thesis'
    elif t in ('incollection', 'inbook'):
        return 'chapter'
    elif t in ('book',):
        return 'book'
    else:
        return 'paper-conference'


def format_authors(author_str):
    """Convert 'Last, First and Last2, First2' to YAML list."""
    if not author_str:
        return ['admin']
    authors = [a.strip() for a in re.split(r'\s+and\s+', author_str, flags=re.IGNORECASE)]
    result = []
    for a in authors:
        if ',' in a:
            parts = [p.strip() for p in a.split(',', 1)]
            result.append(f'{parts[1]} {parts[0]}')
        else:
            result.append(a)
    return result


def yaml_str(s):
    """Escape a string for YAML — wrap in single quotes, escape internal ones."""
    s = s.replace("'", "''")
    return f"'{s}'"


def entry_to_hugo(entry):
    f = entry['fields']

    title = f.get('title', 'Untitled')
    authors = format_authors(f.get('author', ''))
    year = f.get('year', '2024')
    month = f.get('month', '01').replace('jan','01').replace('feb','02').replace('mar','03') \
            .replace('apr','04').replace('may','05').replace('jun','06') \
            .replace('jul','07').replace('aug','08').replace('sep','09') \
            .replace('oct','10').replace('nov','11').replace('dec','12')
    if not month.isdigit():
        month = '01'
    month = month.zfill(2)

    date = f'{year}-{month}-01'
    doi = f.get('doi', '')
    url = f.get('url', f.get('eprint', ''))
    if url and 'arxiv' in url.lower() and not url.startswith('http'):
        url = f'https://arxiv.org/abs/{url}'
    abstract = f.get('abstract', '')

    # Venue
    venue = f.get('journal', f.get('booktitle', f.get('publisher', '')))
    venue_short = f.get('journal_abbrev', f.get('abbr', ''))

    ptype = pub_type(entry['type'], f)

    author_lines = '\n'.join(f'  - {yaml_str(a)}' for a in authors)

    content = f"""---
title: {yaml_str(title)}
authors:
{author_lines}
date: '{date}T00:00:00Z'
doi: '{doi}'
publishDate: '{date}T00:00:00Z'
publication_types:
  - {ptype}
publication: {yaml_str(venue)}
publication_short: {yaml_str(venue_short)}
abstract: {yaml_str(abstract)}
featured: false
tags: []
url_pdf: '{url}'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---
"""
    return content


def main():
    parser = argparse.ArgumentParser(description='Convert BibTeX to HugoBlox publication pages')
    parser.add_argument('bibfile', help='Path to .bib file')
    parser.add_argument('--outdir', default='content/publication', help='Output directory (default: content/publication)')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing entries')
    args = parser.parse_args()

    with open(args.bibfile, 'r', encoding='utf-8') as fh:
        bib_text = fh.read()

    entries = parse_bibtex(bib_text)
    print(f'Found {len(entries)} entries in {args.bibfile}')

    created, skipped = 0, 0
    for entry in entries:
        if entry['type'] in ('string', 'preamble', 'comment'):
            continue
        slug = make_slug(entry['key'], entry['fields'].get('title', ''))
        out_dir = os.path.join(args.outdir, slug)
        out_file = os.path.join(out_dir, 'index.md')

        if os.path.exists(out_file) and not args.overwrite:
            print(f'  SKIP  {slug}  (already exists, use --overwrite to replace)')
            skipped += 1
            continue

        os.makedirs(out_dir, exist_ok=True)
        content = entry_to_hugo(entry)
        with open(out_file, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'  OK    {slug}')
        created += 1

    print(f'\nDone: {created} created, {skipped} skipped.')
    print(f'Now run: git add content/publication/ && git commit -m "Update publications" && git push')


if __name__ == '__main__':
    main()
