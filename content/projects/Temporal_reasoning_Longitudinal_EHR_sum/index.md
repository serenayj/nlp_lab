---
title: Temporal Reasoning for Longitudinal EHR Summarization and Prediction  
date: 2026-01-12
authors:
  - admin
---

*Project theme*: Understanding how large language models reason over time in complex, real-world electronic health records (EHRs).

## Project Motivation

Clinical care unfolds over days to weeks, not single notes. Diagnoses emerge, treatments change, and patient status evolves. While large language models (LLMs) have shown promise for clinical summarization, it remains unclear whether they can truly reason over longitudinal patient trajectories—integrating scattered events, recognizing temporal progression, and avoiding misleading shortcuts when contexts become long and complex.

This project asks a fundamental question:

#### Do today’s LLMs actually understand time in EHRs, or are they just good at reading long text?

## What We Studied

We conducted a systematic evaluation of open-source LLMs on long-context clinical summarization and prediction tasks, redesigned to explicitly stress temporal reasoning. Using two publicly available EHR datasets, we reformulated classic clinical NLP tasks—such as discharge summarization and diagnosis prediction—into longitudinal settings where models must integrate:
  - Structured data (labs, vitals, demographics)
  - Unstructured clinical notes
  - Events distributed across an entire hospital stay

We compared multiple modeling strategies, including:
  - Standard long-context LLM prompting
  - Retrieval-Augmented Generation (RAG)
  - Chain-of-Thought (CoT) prompting

## Key Findings

 - Longer context helps input integration, but not reasoning.
 - Models can read more data, but often fail to correctly track disease progression or temporal dependencies.
 - Temporal reasoning remains a major bottleneck.
 - Errors frequently arise from misordered events, missed clinical turning points, or over-reliance on recent notes.
 - RAG reduces hallucinations—but doesn’t solve the problem.
 - External retrieval improves factual grounding, yet temporal and causal understanding still breaks down in long trajectories.
 - Rare conditions and subtle clinical changes are especially challenging, highlighting risks for real-world deployment.

## Why This Matters

This project provides one of the first systematic stress tests of LLM temporal reasoning in longitudinal EHRs. The results show that simply scaling context length or adding retrieval is not enough for safe clinical use. Instead, new modeling, representation, and evaluation approaches are needed—particularly for high-stakes settings like critical care.

## Broader Impact
Our findings directly inform LARK Lab’s broader research agenda on:
  - Longitudinal patient trajectory modeling
  - Temporal and causal reasoning in clinical NLP
  - Evaluation frameworks for trustworthy medical AI
  - Safer deployment of LLMs in clinical decision support and caregiver-facing tools

## Publication

This project was published as a Findings paper at EMNLP 2025, contributing benchmarks and empirical insights for the NLP and clinical AI communities.
