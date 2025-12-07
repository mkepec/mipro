#!/usr/bin/env python3
"""
Analyze MIPRO Junior papers for patterns, complexity, and topics
"""

import re
from pathlib import Path
from collections import defaultdict, Counter

def extract_papers_by_year(content):
    """Extract papers organized by year"""
    papers_by_year = defaultdict(list)
    current_year = None

    lines = content.split('\n')
    for line in lines:
        # Detect year headers
        if re.match(r'^## \d{4}$', line):
            current_year = int(line.replace('##', '').strip())
        # Collect paper titles (lines starting with *   **Paper Title)
        elif current_year and line.strip().startswith('*   **'):
            title = re.search(r'\*\*(.+?)\*\*', line)
            if title:
                papers_by_year[current_year].append(title.group(1))

    return papers_by_year

def categorize_by_keywords(title):
    """Categorize papers by topic based on title keywords"""
    title_lower = title.lower()
    categories = []

    # Technology categories
    if any(word in title_lower for word in ['cloud', 'aws', 'azure', 'google cloud']):
        categories.append('Cloud Computing')

    if any(word in title_lower for word in ['ai', 'artificial intelligence', 'machine learning', 'deep learning', 'neural', 'llm', 'gpt', 'chatgpt']):
        categories.append('AI/ML')

    if any(word in title_lower for word in ['iot', 'sensor', 'arduino', 'raspberry', 'embedded', 'microcontroller']):
        categories.append('IoT/Embedded')

    if any(word in title_lower for word in ['mobile', 'android', 'ios', 'app']):
        categories.append('Mobile Development')

    if any(word in title_lower for word in ['web', 'website', 'html', 'javascript', 'react']):
        categories.append('Web Development')

    if any(word in title_lower for word in ['network', '5g', 'wifi', 'protocol', 'communication']):
        categories.append('Networking')

    if any(word in title_lower for word in ['security', 'cyber', 'encryption', 'attack', 'vulnerability']):
        categories.append('Cybersecurity')

    if any(word in title_lower for word in ['database', 'sql', 'data', 'analytics']):
        categories.append('Data/Database')

    if any(word in title_lower for word in ['game', 'gaming', 'virtual reality', 'vr', 'ar', 'augmented reality']):
        categories.append('Gaming/VR/AR')

    if any(word in title_lower for word in ['electric', 'energy', 'power', 'renewable', 'solar', 'wind']):
        categories.append('Energy/Power Systems')

    if any(word in title_lower for word in ['image', 'vision', 'detection', 'recognition', 'opencv']):
        categories.append('Computer Vision')

    if any(word in title_lower for word in ['robot', 'autonomous', 'drone', 'uav']):
        categories.append('Robotics/Autonomous Systems')

    if any(word in title_lower for word in ['performance', 'optimization', 'evaluation', 'comparison', 'benchmarking']):
        categories.append('Performance/Optimization')

    if any(word in title_lower for word in ['education', 'teaching', 'learning', 'student']):
        categories.append('Education')

    # Complexity indicators
    if any(word in title_lower for word in ['comparative', 'comparison', 'analysis', 'study', 'evaluation', 'assessment']):
        categories.append('[Type: Comparative Study]')

    if any(word in title_lower for word in ['implementation', 'development', 'design', 'system', 'application']):
        categories.append('[Type: Implementation]')

    if any(word in title_lower for word in ['optimization', 'optimizing', 'improving', 'enhancing', 'performance']):
        categories.append('[Type: Optimization]')

    return categories if categories else ['Other']

def assess_complexity(title):
    """Assess paper complexity based on title"""
    title_lower = title.lower()

    # Simple indicators
    simple_keywords = ['introduction', 'overview', 'basic', 'simple', 'awareness']

    # Medium indicators
    medium_keywords = ['implementation', 'development', 'application', 'system', 'analysis', 'comparison']

    # Complex indicators
    complex_keywords = ['optimization', 'novel', 'advanced', 'framework', 'algorithm', 'multi-', 'comprehensive']

    if any(word in title_lower for word in complex_keywords):
        return 'Complex'
    elif any(word in title_lower for word in medium_keywords):
        return 'Medium'
    elif any(word in title_lower for word in simple_keywords):
        return 'Simple'
    else:
        return 'Medium'  # Default

def main():
    junior_file = Path('mipro_junior_papers.md')
    output_file = Path('research/analysis/junior_papers_analysis.md')

    content = junior_file.read_text(encoding='utf-8')
    papers_by_year = extract_papers_by_year(content)

    # Collect statistics
    total_papers = sum(len(papers) for papers in papers_by_year.values())
    all_categories = []
    all_complexities = []
    cloud_aws_papers = []

    for year, papers in papers_by_year.items():
        for paper in papers:
            categories = categorize_by_keywords(paper)
            all_categories.extend(categories)
            complexity = assess_complexity(paper)
            all_complexities.append(complexity)

            # Track cloud/AWS papers
            paper_lower = paper.lower()
            if any(word in paper_lower for word in ['cloud', 'aws', 'azure']):
                cloud_aws_papers.append((year, paper))

    # Count categories
    category_counter = Counter(all_categories)
    complexity_counter = Counter(all_complexities)

    # Write analysis
    with output_file.open('w', encoding='utf-8') as f:
        f.write("# MIPRO Junior Papers Analysis (2010-2025)\n\n")
        f.write("## Overview\n\n")
        f.write(f"- Total papers analyzed: {total_papers}\n")
        f.write(f"- Years covered: {min(papers_by_year.keys())}-{max(papers_by_year.keys())}\n")
        f.write(f"- Average papers per year: {total_papers / len(papers_by_year):.1f}\n\n")

        f.write("## Papers per Year\n\n")
        for year in sorted(papers_by_year.keys(), reverse=True):
            f.write(f"- **{year}**: {len(papers_by_year[year])} papers\n")

        f.write("\n---\n\n")
        f.write("## Complexity Distribution\n\n")
        for complexity, count in complexity_counter.most_common():
            percentage = (count / total_papers) * 100
            f.write(f"- **{complexity}**: {count} papers ({percentage:.1f}%)\n")

        f.write("\n**Complexity Assessment Criteria:**\n")
        f.write("- **Simple**: Introductory topics, basic implementations, surveys\n")
        f.write("- **Medium**: Full implementations, comparative studies, analysis\n")
        f.write("- **Complex**: Optimizations, novel algorithms, multi-component systems\n\n")

        f.write("---\n\n")
        f.write("## Topic Distribution\n\n")

        # Separate topic categories from paper types
        topic_cats = {k: v for k, v in category_counter.items() if not k.startswith('[')}
        type_cats = {k: v for k, v in category_counter.items() if k.startswith('[')}

        f.write("### Technology Topics\n\n")
        for category, count in sorted(topic_cats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_papers) * 100
            f.write(f"- **{category}**: {count} papers ({percentage:.1f}%)\n")

        f.write("\n### Paper Types\n\n")
        for category, count in sorted(type_cats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_papers) * 100
            category_name = category.replace('[Type: ', '').replace(']', '')
            f.write(f"- **{category_name}**: {count} papers ({percentage:.1f}%)\n")

        f.write("\n---\n\n")
        f.write("## Cloud/AWS Related Papers\n\n")
        f.write(f"**Total**: {len(cloud_aws_papers)} papers\n\n")

        if cloud_aws_papers:
            for year, paper in sorted(cloud_aws_papers, key=lambda x: x[0], reverse=True):
                f.write(f"- **{year}**: {paper}\n")
        else:
            f.write("*No cloud/AWS-related papers found*\n")

        f.write("\n---\n\n")
        f.write("## Student-Suitable Topics for 2nd Year Undergrads (SW Developers)\n\n")
        f.write("Based on the analysis, here are suitable project types:\n\n")

        f.write("### Recommended Topic Areas (Based on Historical Trends)\n\n")
        f.write("1. **IoT/Embedded Projects** (Most common - good for hands-on)\n")
        f.write("   - Arduino/Raspberry Pi-based systems\n")
        f.write("   - Sensor data collection and monitoring\n")
        f.write("   - Smart device implementations\n\n")

        f.write("2. **AI/ML Applications** (Growing trend)\n")
        f.write("   - Using ChatGPT/LLM APIs for applications\n")
        f.write("   - Simple ML models for classification\n")
        f.write("   - Image/text processing with existing libraries\n\n")

        f.write("3. **Web/Mobile Development** (Strong presence)\n")
        f.write("   - Web applications with database backend\n")
        f.write("   - Mobile apps for specific use cases\n")
        f.write("   - Performance comparisons of frameworks\n\n")

        f.write("4. **Performance/Comparative Studies** (Very common)\n")
        f.write("   - Comparing different technologies/approaches\n")
        f.write("   - Benchmarking tools/frameworks\n")
        f.write("   - Evaluation of existing solutions\n\n")

        f.write("### Cloud/AWS Opportunities (GAP IDENTIFIED!)\n\n")
        f.write(f"**Current state**: Only {len(cloud_aws_papers)} cloud-related papers out of {total_papers} total\n\n")
        f.write("**Opportunities for your students:**\n")
        f.write("1. AWS-based IoT data collection and visualization\n")
        f.write("2. Serverless application development (Lambda, API Gateway)\n")
        f.write("3. Cloud vs on-premise performance comparison\n")
        f.write("4. Containerized application deployment (ECS, ECR)\n")
        f.write("5. AWS services integration projects (S3, DynamoDB, SNS)\n")
        f.write("6. Cloud security basics implementation\n")
        f.write("7. Infrastructure-as-Code simple projects (CloudFormation, CDK basics)\n\n")

        f.write("### Complexity Recommendations\n\n")
        f.write("For 2nd year undergrads, target **Medium complexity** papers:\n")
        f.write("- Full working implementation (not just overview)\n")
        f.write("- Clear problem statement and solution\n")
        f.write("- Measurable results (performance, functionality)\n")
        f.write("- Avoid: Novel algorithms, complex optimizations\n")
        f.write("- Focus: Practical applications, comparative studies, integrations\n\n")

    print(f"✓ Analysis complete: {output_file}")
    print(f"\nKey Findings:")
    print(f"- Total papers: {total_papers}")
    print(f"- Cloud/AWS papers: {len(cloud_aws_papers)} ({(len(cloud_aws_papers)/total_papers)*100:.1f}%)")
    print(f"- Most common topic: {topic_cats.most_common(1)[0] if topic_cats else 'N/A'}")
    print(f"- Complexity distribution: {dict(complexity_counter)}")

if __name__ == '__main__':
    main()
