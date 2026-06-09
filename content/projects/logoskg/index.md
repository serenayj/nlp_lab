---
title: "LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval"
date: 2026-06-09
author: Yanjun Gao, PhD; He Cheng, PhD
tags: [knowledge graphs, LLMs, biomedical NLP, scalability, KG-LLM integration]
---

*Project theme*: Enabling scalable, interpretable multi-hop retrieval over large biomedical knowledge graphs as a foundation for trustworthy KG-LLM integration.

*Lead*: This project was led by He Cheng, Postdoctoral Researcher at the LARK Lab. 

## Project Motivation

Integrating knowledge graphs (KGs) with large language models (LLMs) is one of the most promising paths toward structured, verifiable biomedical reasoning. The central operation in this integration is multi-hop retrieval: starting from a query entity, traversing chains of relations across genes, pathways, diseases, and therapies to surface relevant evidence. Yet existing systems cannot simultaneously satisfy three basic requirements: they are either efficient but opaque, interpretable but slow, or scalable but approximate.

This limitation is not incidental. It reflects a mismatch between how KG traversal is conventionally implemented — as iterative graph database queries, and how modern hardware actually executes computation. At billion-edge scale, conventional approaches become slow and memory-intensive. Interpretability is sacrificed for speed, or scale is sacrificed for faithfulness.

This project asks a precise question:

#### Can multi-hop KG retrieval be made simultaneously efficient, scalable, and interpretable — without trading one off against the others?

## What We Built

We introduce **LogosKG**, a hardware-aligned framework that reformulates k-hop KG traversal as a sequence of hardware-efficient matrix operations over decomposed subject, object, and relation representations. By grounding traversal in symbolic KG formulations rather than neural approximations, LogosKG preserves full interpretability: every retrieved path is an exact, traceable chain of relations.

To scale to billion-edge graphs, LogosKG integrates three mechanisms:

- **Degree-aware partitioning** — distributes graph structure across memory hierarchies in proportion to node connectivity, avoiding bottlenecks at high-degree hubs.
- **Cross-graph routing** — enables traversal across heterogeneous KG sources without requiring a unified index, supporting multi-source biomedical KGs.
- **On-demand caching** — loads subgraph neighborhoods lazily, reducing peak memory footprint for sparse traversal patterns.

Together, these allow LogosKG to perform chained inferences across genes, pathways, diseases, and therapies on a single workstation at scales previously requiring distributed infrastructure.

## Key Results

- **Substantial efficiency gains** over CPU and GPU baselines across k-hop retrieval benchmarks, with no loss of retrieval fidelity relative to exact methods.
- **Billion-edge scalability** demonstrated on large biomedical KGs, with latency and memory costs substantially lower than Neo4j and GPU-accelerated graph frameworks.
- **KG-LLM interaction analysis**: a two-round pipeline using LogosKG reveals how KG topology shapes the alignment between structured biomedical knowledge and LLM diagnostic reasoning. Dense, well-studied regions of the KG produce high LLM-KG alignment; sparse regions expose the limits of LLM biomedical knowledge.

## Why This Matters

Most current KG-LLM integration work treats the KG as a static retrieval index and the LLM as a fixed reasoner. LogosKG enables a different relationship: because retrieval is fast, interpretable, and scalable, it becomes feasible to study how the *structure* of the KG shapes LLM reasoning, and to design integration strategies that account for that structure rather than ignoring it.

This has direct implications for biomedical discovery. When LLM reasoning is anchored to KG regions with dense, well-curated evidence, it is more reliable. When it ventures into sparse, long-tail regions, it is more likely to hallucinate or confabulate. LogosKG makes this distinction visible and actionable.

## Connection to Broader Research

LogosKG is the scalable knowledge substrate underlying our AI4Science research program. It directly addresses the alignment coverage and scalability gap, and provides the retrieval foundation for the multi-step reasoning.

## Publication

**LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval**  
LARK Lab, University of Colorado Anschutz  
*ACL 2026 (Main Conference)*

- **Paper:** [openreview.net/forum?id=AvpJrTtFKb](https://arxiv.org/abs/2604.18913)
- **Keywords:** knowledge graphs, neurosymbolic approaches, biomedical knowledge graphs, clinical NLP, hardware-efficient inference 
