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

abstract: Large language models (LLMs) often behave inconsistently across inputs, indicating uncertainty and motivating the need for its quantification in high-stakes settings. Prior work on calibration and uncertainty quantification often focuses on individual models, overlooking the potential of model diversity. We hypothesize that LLMs make complementary predictions due to differences in training and the Zipfian nature of language, and that aggregating their outputs leads to more reliable uncertainty estimates. To leverage this, we propose MUSE (Multi-LLM Uncertainty via Subset Ensembles), a simple information-theoretic method that uses Jensen-Shannon Divergence to identify and aggregate well-calibrated subsets of LLMs. Experiments on binary prediction tasks demonstrate improved calibration and predictive performance compared to single-model and naive ensemble baselines. In addition, we explore using MUSE as guided signals with chain-of-thought distillation to fine-tune LLMs for calibration. 

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
Large language models (LLMs) are increasingly used in high-stakes settings, and a key question is: how confident are they in their predictions? This paper argues that most prior work focuses on calibration and uncertainty quantification for individual models, and often ignores the potential benefit of model diversity.
The authors posit that because different LLMs are trained differently (and language itself is Zipfian), their predictions will differ in complementary ways. The key idea: leverage that diversity by aggregating subsets of LLMs to produce better uncertainty estimates.
To this end, the paper proposes MUSE (Multi-LLM Uncertainty via Subset Ensembles) — an information-theoretic method that uses Jensen-Shannon Divergence (JSD) to pick well-calibrated subsets of LLMs and then aggregate their predictions.
Empirically, the work shows that on binary prediction tasks, using MUSE improves both calibration and predictive performance compared to a single model or a naive ensemble. Additionally, they explore using MUSE’s outputs to fine-tune (via chain-of-thought distillation) an LLM specifically for calibration.

Why does this matter for our lab? 
  -  The theme aligns directly with our interest in LLM calibration and uncertainty estimation, especially in applied domains (e.g., clinical or critical‐care settings).
  -  It shifts the lens from “one LLM behaving badly/unreliable” to “multiple LLMs collaborating/being aggregated”. This opens new design space: ensemble strategies, subset selection, metrics beyond accuracy.
  -  The use of an information‐theoretic metric (JSD) for subset identification is elegant and theoretically grounded — so there may be opportunities to generalize or adapt to our own multi-model pipelines (e.g., multi‐agent LLMs in ICU decision support).
  -  The fine‐tuning via chain-of-thought distilled from the ensemble is interesting: suggests that uncertainty‐aware calibration isn’t only a post-hoc measure, but can be baked into model training.
