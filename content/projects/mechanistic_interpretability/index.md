---
title: Analyzing GPT-2's Positional Bias on Multiple Choice Question Answering using Mechanistic Interpretability  
date: 2024-05-07
authors:
  - admin
---

Large Language Models (LLMs) like GPT-4 have demonstrated significant advancements in tasks such as Multiple Choice Question (MCQ) Answering, including those within medical domains like MedQA. However, our recent research reveals a positional bias in earlier models such as GPT-2, where they consistently select the first answer choice ("A") regardless of the actual correct answer's position. This bias substantially undermines their effectiveness in MCQ scenarios.

To pinpoint the origins of this bias and devise strategies to counteract it, we employed techniques from Mechanistic Interpretability to analyze each layer of the LLMs. By assessing the logit differences between the biased (anchored) answer and the correct answer options, we identified which layers exhibit stronger biases. Notably, we discovered significant contributions to the bias from the Multi-Layer Perceptron (MLP) weights and certain attention head weights.

To address this issue, we implemented an intervention that involves adjusting the MLP and attention head weights by subtracting the values linked to the anchored bias from those corresponding to the correct answer options. This corrective action has proven effective in enhancing the performance of the GPT-2 model family and reducing the positional bias.

This work is collaborated with Dr. Ruizhe Li, at University of Aberdeen. We recently release the preprint at: [https://arxiv.org/abs/2405.03205](https://arxiv.org/abs/2405.03205).  

