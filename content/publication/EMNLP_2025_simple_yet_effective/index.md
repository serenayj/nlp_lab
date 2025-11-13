---
title: "Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
# example: admin 
authors:
  - maya_kruse
  - Majid Afshar
  - saksham_khatwani
  - Anoop Mayampurath
  - Guanhua Chen
  - admin

# Author notes (optional)
#author_notes:
#  - 'Equal contribution'
#  - 'Equal contribution'

date: '2024-11-12T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
#publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Findings of the Association of Computational Linguistics Empirical Methods in Natural Language Processing 2024*
publication_short: In *Findings of EMNLP 2024*

abstract: Large language models (LLMs) are increasingly used in high-stakes settings, and a key question is, how confident are they in their predictions? This paper argues that most prior work focuses on calibration and uncertainty quantification for individual models, and often ignores the potential benefit of model diversity.

# Summary. An optional shortened abstract.
#summary:


#tags: ["large language models", "machine learning", "eletronic health records", "clinical informatics"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://aclanthology.org/2025.emnlp-main.1551.pdf'
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_poster: ''
#url_project: ''
#url_slides: ''
url_source: 'https://aclanthology.org/2025.emnlp-main.1551/'
#url_video: 'https://www.youtube.com/watch?v=NX1nEm90mSQ&t=1s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Comparative results of supervised fine-tuning with MUSE-derived probabilities'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---
Why does this matter for our lab?
  -  The theme aligns directly with our interest in LLM calibration and uncertainty estimation, especially in applied domains (e.g., clinical or critical‐care settings).
  -  It shifts the lens from “one LLM behaving badly/unreliable” to “multiple LLMs collaborating/being aggregated”. This opens new design space: ensemble strategies, subset selection, metrics beyond accuracy.
  -  The use of an information‐theoretic metric (JSD) for subset identification is elegant and theoretically grounded — so there may be opportunities to generalize or adapt to our own multi-model pipelines (e.g., multi‐agent LLMs in ICU decision support).
  -  The fine‐tuning via chain-of-thought distilled from the ensemble is interesting: suggests that uncertainty‐aware calibration isn’t only a post-hoc measure, but can be baked into model training.
