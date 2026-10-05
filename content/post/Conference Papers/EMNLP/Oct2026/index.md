---
title: "Under the Hood of LLMs: LARK Lab at EMNLP 2026"
date: 2026-10-05
authors:
  - saksham_khatwani
  - shiyue_hu
  - admin
---

We are excited to share two LARK Lab papers accepted to EMNLP 2026 in Budapest, Hungary!

This year, our work at EMNLP shares a common theme: **What’s under the hood of large language models?**

Benchmark performance tells us what an LLM can do. But for models increasingly used in healthcare and other high-stakes settings, performance alone is not enough. We also want to understand what changes inside a model when we train it with external knowledge, where socially meaningful information is represented, and how those internal mechanisms ultimately shape model behavior.

Our two EMNLP papers approach these questions from two complementary directions: **knowledge injection and optimization geometry**, and **demographic bias and mechanistic interpretability**.

These papers are also particularly special to us because both were led by researchers who started the work while they were still graduate students. **Saksham Khatwani** led our work on surgical alignment, and **Shiyue Hu** led our work on demographic bias. Both projects grew substantially over time, through many rounds of experiments, new questions, and revisions. Their paths to EMNLP reflect not only strong research, but also the **stamina** it takes to stay with a difficult question and keep pushing it forward.


## 🩺 Paper 1: Knowledge Injection × Optimization Geometry

### Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models

**First author: Saksham Khatwani**

How does injecting structured biomedical knowledge actually reshape an LLM?

In this work, we systematically study knowledge graph (KG) training for clinical diagnosis across multiple task formulations, training paradigms, knowledge graphs, and base LLMs. Beyond downstream accuracy, we introduce two optimization-geometry measures — **Gradient Intervention Density (GID)** and **Gradient Distortion (GD)** — to characterize how different training objectives modify the model.

Our results reveal an interesting distinction: KG-judgment training with KL regularization produces sparse, localized parameter updates, a phenomenon we call **surgical alignment**, while conventional task-specific supervised fine-tuning produces much denser changes.

Importantly, these internal differences matter. The sparse regimes show stronger transfer and reasoning quality even when they do not achieve the highest in-domain accuracy, suggesting that *how* knowledge changes a model can be as important as whether its benchmark score improves.

📄 Paper (preprint) : https://arxiv.org/abs/2608.26587  
💻 Code: https://github.com/LARK-NLP-Lab/Surgical-Alignment


## 🔍 Paper 2: Demographic Bias × Mechanistic Interpretability

### Tracing the Latent Threads: A Mechanistic Study of How LLMs Represent and Operationalize Race and Ethnicity Cues

**First author: Shiyue Hu**

Where do demographic cues live inside an LLM — and how do they influence what the model ultimately predicts?

Most studies of demographic bias focus on disparities observed at the model output. In this work, we instead trace race and ethnicity cues *inside* three open-source LLMs across toxicity-related generation and clinical narrative understanding.

Using probing, neuron-level attribution, logit-lens analysis, and targeted interventions, we examine how demographic information is represented and operationalized throughout the model.

We find that sensitivity to race and ethnicity cues is not confined to a small, easily identifiable set of neurons. Instead, it is distributed across many units, varies substantially across models, and is entangled with related concepts including geography, language, culture, and stereotypes. Intervening on selected neurons can shift some biased predictions, but substantial residual effects remain.

These findings highlight both the promise — and the limitations — of localized mechanistic interventions for understanding and mitigating demographic bias in LLMs.

📄 Paper (preprint): https://arxiv.org/abs/2601.12868  
💻 Code: https://github.com/LARK-NLP-Lab/LLM-Bias-Interpretability


## 🔧 What’s Under the Hood?

Although these two projects began with very different questions, they converge on a common lesson:

**Model outputs tell only part of the story.**

Two training strategies can produce similar benchmark performance while changing a model in very different ways. Likewise, demographic bias observed at the output can arise from representations distributed throughout a model rather than from a small, easily isolated set of components.

Understanding trustworthy LLMs therefore requires us to study not only **what models do**, but also **how training changes them, what they represent internally, and how those representations become behavior**.

This perspective is becoming an increasingly important part of LARK Lab's research agenda, connecting our work in clinical NLP and knowledge-grounded reasoning with optimization, mechanistic interpretability, uncertainty, and trustworthy AI.


## ✨ Celebrating the People Behind the Work

A special congratulations to **Saksham Khatwani** and **Shiyue Hu**, the first authors of these two papers.

Both projects have a history behind them. Saksham and Shiyue began building these lines of work while they were still graduate students and continued pushing them forward as the questions, methods, and scope evolved.

Research papers tend to celebrate the final result. But getting to that result often depends on something less visible: the **stamina to stay with a hard problem**, to keep asking better questions when the first answers are incomplete, and to continue refining an idea until the story becomes clear.

Saksham and Shiyue have both shown that stamina, together with the intellectual curiosity and independence that make strong researchers. We are very proud to see these projects reach EMNLP.

Congratulations as well to **He Cheng** for his contributions to this work and to the broader research behind these projects.


## ⭐ Acknowledgements

We are deeply grateful to our collaborators and co-authors **Dr. Majid Afshar (UW-Madison), Dr. Dmitriy Dligach (Loyola Chicago), and Dr. Ruizhe Li (University of Birmingham**. Their expertise, ideas, and continued collaboration have been invaluable in bringing these projects to fruition.

We look forward to presenting both papers at **EMNLP 2026 in Budapest**. Come find us and talk with us about knowledge injection, optimization geometry, mechanistic interpretability, demographic bias — or what else might be hiding under the hood of LLMs!
