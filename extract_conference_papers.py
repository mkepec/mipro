#!/usr/bin/env python3
"""
Extract MIPRO conference papers by conference track and year
"""

import re
from pathlib import Path
from collections import defaultdict

# Target conferences with all name variations
CONFERENCES = {
    'SSE': {
        'name': 'Software and Systems Engineering',
        'patterns': [
            'SOFTWARE AND SYSTEMS ENGINEERING',
            'Software and Systems Engineering',
            'COMPOSABILITY, COMPREHENSIBILITY AND CORRECTNESS OF WORKING SOFTWARE',
        ]
    },
    'EE': {
        'name': 'Engineering Education',
        'patterns': [
            'ENGINEERING EDUCATION',
            'Engineering Education',
        ]
    },
    'DC-CPS': {
        'name': 'Distributed Computing and Cyber-Physical Systems',
        'patterns': [
            'DISTRIBUTED COMPUTING AND CYBER-PHYSICAL SYSTEMS',
            'Distributed Computing and Cyber-Physical Systems',
            'Distributed Computing and Visualization Systems',
            'DISTRIBUTED COMPUTING IN DATA SCIENCE AND BIOMEDICAL ENGINEERING',
            'DISTRIBUTED COMPUTING, VISUALIZATION AND BIOMEDICAL ENGINEERING',
            'DATA AND LIFE SCIENCES SUPPORTED BY DISTRIBUTED COMPUTING',
        ]
    },
    'CE': {
        'name': 'Computers in Education',
        'patterns': [
            'COMPUTERS IN EDUCATION',
            'Computers in Education',
        ]
    }
}

def extract_conference_section(content, patterns):
    """Extract all papers for a specific conference from markdown content"""
    papers = []
    in_section = False
    current_subsection = None

    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Check if we're entering our target conference section
        if line.startswith('## ') and any(pattern in line for pattern in patterns):
            in_section = True
            continue

        # Check if we're leaving the section (next ## header that's not our conference)
        if in_section and line.startswith('## ') and not any(pattern in line for pattern in patterns):
            break

        # Track subsections (### headers within conference)
        if in_section and line.startswith('### '):
            current_subsection = line.replace('###', '').strip()
            continue

        # Collect paper entries (lines starting with *)
        if in_section and line.strip().startswith('*'):
            # Include subsection info if available
            paper_line = line.strip()
            if current_subsection and not paper_line.startswith('*   **'):
                # Add context if we're in a subsection
                papers.append(paper_line)
            else:
                papers.append(paper_line)

    return papers

def main():
    papers_dir = Path('papers')
    output_dir = Path('research/analysis')
    output_dir.mkdir(parents=True, exist_ok=True)

    years = range(2010, 2026)  # 2010-2025

    for conf_code, conf_info in CONFERENCES.items():
        all_papers = defaultdict(list)
        total_papers = 0

        print(f"\nProcessing {conf_code} - {conf_info['name']}...")

        for year in years:
            year_file = papers_dir / f"{year}.md"
            if not year_file.exists():
                continue

            try:
                content = year_file.read_text(encoding='utf-8')
                papers = extract_conference_section(content, conf_info['patterns'])

                if papers:
                    all_papers[year] = papers
                    total_papers += len(papers)
                    print(f"  {year}: {len(papers)} papers")
            except Exception as e:
                print(f"  {year}: Error - {e}")

        # Write output file
        output_file = output_dir / f"{conf_code}_papers_historical.md"
        with output_file.open('w', encoding='utf-8') as f:
            f.write(f"# {conf_info['name']} - Historical Papers Analysis\n\n")
            f.write(f"## Overview\n")
            f.write(f"- Total papers analyzed: {total_papers}\n")

            if all_papers:
                f.write(f"- Years covered: {min(all_papers.keys())}-{max(all_papers.keys())}\n")
                f.write(f"- Years with papers: {len(all_papers)}\n\n")

                f.write("## Papers per Year\n\n")
                for year in sorted(all_papers.keys(), reverse=True):
                    f.write(f"| {year} | {len(all_papers[year])} papers |\n")
                f.write("\n---\n\n")

                # Write papers by year
                for year in sorted(all_papers.keys(), reverse=True):
                    f.write(f"## {year}\n\n")
                    for paper in all_papers[year]:
                        f.write(f"{paper}\n")
                    f.write("\n")

                # Add quick stats
                f.write("---\n\n")
                f.write("## Quick Stats\n\n")
                peak_year = max(all_papers.keys(), key=lambda y: len(all_papers[y]))
                f.write(f"- Peak year (most papers): {peak_year} ({len(all_papers[peak_year])} papers)\n")

                recent_years = [y for y in all_papers.keys() if y >= 2023]
                if recent_years:
                    recent_count = sum(len(all_papers[y]) for y in recent_years)
                    f.write(f"- Recent activity (2023-2025): {recent_count} papers\n")

                old_years = [y for y in all_papers.keys() if y <= 2015]
                if old_years:
                    old_count = sum(len(all_papers[y]) for y in old_years)
                    f.write(f"- Historical activity (2010-2015): {old_count} papers\n")
            else:
                f.write(f"- No papers found\n")

        print(f"  ✓ Created {output_file}")
        print(f"  Total: {total_papers} papers")

if __name__ == '__main__':
    main()
