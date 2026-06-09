---
title: "LogosKG Accepted at ACL 2026 (Main Conference)"
date: 2026-06-09
authors:
  - admin
---

We are excited to share that our paper **LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval** has been accepted to the main conference at **ACL 2026**.

Knowledge graphs (KGs) are a critical substrate for grounding LLM reasoning in structured, verifiable evidence, but existing systems struggle to balance efficiency, scalability, and interpretability when performing multi-hop retrieval at biomedical scale. LogosKG addresses this directly: it is a hardware-aligned framework that executes k-hop traversal as efficient operations over decomposed symbolic representations, integrates degree-aware partitioning and on-demand caching to scale to billion-edge graphs, and achieves substantial efficiency gains over both CPU and GPU baselines without sacrificing retrieval fidelity.

Beyond retrieval, the paper demonstrates a two-round KG-LLM interaction pipeline that uses LogosKG to analyze how KG topology (hop distribution, connectivity patterns) shapes alignment between structured biomedical knowledge and LLM diagnostic reasoning, opening a concrete path toward next-generation KG-LLM integration.

This work is foundational to our broader AI4Science research program on scalable, interpretable biomedical knowledge infrastructure.

**[Read the paper →](https://arxiv.org/abs/2604.18913)**  

**[Try online demo →](https://lark-nlp-lab-logoskg.hf.space)**   
