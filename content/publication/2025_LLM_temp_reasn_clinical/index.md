---
title: "Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
# example: admin 
authors:
  - maya_kruse
  - shiyue_hu
  - nicolas_derby
  - yifu_wu
  - Samantha Stonbraker
  - Bingsheng Yao
  - Dakuo Wang
  - Elizabeth Goldberg
  - admin

# Author notes (optional)
#author_notes:
#  - 'Equal contribution'
#  - 'Equal contribution'

date: '2025-09-04T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
#publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article']

# Publication name and optional abbreviated publication name.
#publication:""
#publication_short: ""

abstract: Recent advances in large language models (LLMs) have shown potential in clinical text summarization, but their ability to handle long patient trajectories with multi-modal data spread across time remains underexplored. This study systematically evaluates several state-of-the-art open-source LLMs, their Retrieval Augmented Generation (RAG) variants and chain-of-thought (CoT) prompting on long-context clinical summarization and prediction. We examine their ability to synthesize structured and unstructured Electronic Health Records (EHR) data while reasoning over temporal coherence, by re-engineering existing tasks, including discharge summarization and diagnosis prediction from two publicly available EHR datasets. Our results indicate that long context windows improve input integration but do not consistently enhance clinical reasoning, and LLMs are still struggling with temporal progression and rare disease prediction. While RAG shows improvements in hallucination in some cases, it does not fully address these limitations. Our work fills the gap in long clinical text summarization, establishing a foundation for evaluating LLMs with multi-modal data and temporal reasoning.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: ["large language models", "electronic health records", "clinical informatics"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/abs/2501.18724'
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_video: 'https://www.youtube.com/watch?v=NX1nEm90mSQ&t=1s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'An illustration of the longitudinal patient trajectory summarization process from multi-modal EHRs.'
  focal_point: ''
  preview_only: false
---
