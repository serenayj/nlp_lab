# Uncertainty Quantification for Large Language Models: MUSE, a Multi-LLM Subset Ensemble Approach

*Project theme*: Uncertainty quantification (UQ) and calibration for large language models — a simple, information-theoretic method that aggregates multiple LLMs for reliable confidence estimates in high-stakes decision-making.

*Lead*: This project was led by Maya Kruse, a former NLP Data Scientist at the LARK Lab.

## Project Motivation

Large language models often behave inconsistently across inputs—a signal of underlying uncertainty that matters enormously in high-stakes settings like clinical decision support. **Uncertainty quantification (UQ)**—estimating how much to trust a model's prediction—is therefore a prerequisite for safe LLM deployment. Yet most existing uncertainty quantification and calibration methods focus on individual models, ignoring a valuable resource: model diversity. Because LLMs differ in training data, architecture, and scale—and because language itself follows a Zipfian distribution—different models make complementary predictions.

This project asks a fundamental question:

#### Can we get more reliable uncertainty estimates by intelligently combining multiple LLMs, rather than trusting any single one?

## What We Did

We propose **MUSE** (Multi-LLM Uncertainty via Subset Ensembles), a simple information-theoretic framework for multi-LLM uncertainty quantification that:

- Uses **Jensen-Shannon Divergence** to measure agreement among candidate LLMs
- Identifies **well-calibrated subsets** of models rather than naively averaging all of them
- Aggregates subset outputs into a single, more reliable uncertainty estimate

Beyond post-hoc estimation, we also explored using MUSE-derived uncertainty as **guided signals for chain-of-thought distillation**, fine-tuning LLMs to be better calibrated by construction.

## Key Findings

- **Subset selection beats naive ensembling.** Aggregating only well-calibrated model subsets improves both calibration and predictive performance over single models and full ensembles on binary prediction tasks.
- **Model diversity is a feature, not a bug.** Complementary errors across LLMs can be exploited systematically with a principled information-theoretic criterion.
- **Uncertainty signals can teach models.** Using MUSE as supervision in chain-of-thought distillation offers a path toward LLMs that are calibrated at inference time without ensemble overhead.
- **Simplicity matters.** MUSE requires no architectural changes or access to model internals, making it portable across model families and application domains.

## Why This Matters

Deploying LLMs in high-stakes domains requires knowing not just what a model predicts, but how much to trust that prediction. MUSE provides a lightweight, generalizable uncertainty quantification method that works with off-the-shelf models—no access to model internals required—making it an essential building block for safe AI-assisted decision-making in medicine and beyond.

## Broader Impact

This work anchors LARK Lab's broader research agenda on uncertainty quantification for trustworthy AI—spanning calibration of clinical LLMs, communicating model confidence to clinicians, and calibration-aware fine-tuning and distillation.

## Publication

This project was published at **EMNLP 2025** (main conference).

Maya Kruse, Majid Afshar, Saksham Khatwani, Anoop Mayampurath, Guanhua Chen, and Yanjun Gao. 2025. [Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification](https://aclanthology.org/2025.emnlp-main.1551/). In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 30493–30504.

Code: [https://github.com/LARK-NLP-Lab/MUSE](https://github.com/LARK-NLP-Lab/MUSE)
