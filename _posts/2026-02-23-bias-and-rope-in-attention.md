---
layout: distill
title: Handling Bias and RoPE in QK Attention with a Unified Geometric View
description: A practical geometric view for analyzing QK circuits with bias and RoPE using a single bilinear form
tags:
  - mechanistic interpretability
  - transformers
  - attention
  - linear algebra
giscus_comments: true
date: 2026-02-23
featured: false

authors:
  - name: Gabriel Franco
    affiliations:
      name: Department of Computer Science, Boston University

bibliography: pinpointing-attention.bib

toc:
  - name: "1. QK attention as a bilinear map"
  - name: "2. Related work on SVD of QK"
  - name: "3. Why bias and position terms make QK analysis harder"
  - name: "4. Bias: translate first, then project"
  - name: "5. RoPE: rotate first, then project"
  - name: "6. Appendix: condition numbers in practice"

_styles: >
  .callout {
    padding: 14px 16px;
    border: 1px solid rgba(0,0,0,0.12);
    border-radius: 10px;
    background: rgba(0,0,0,0.02);
    margin: 18px 0;
  }
  .callout strong {
    display: block;
    margin-bottom: 6px;
  }
  .qk-img-white {
    background: #ffffff;
    padding: 8px;
  }
  .caption {
    color: var(--global-text-color) !important;
  }
  .cond-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    align-items: start;
  }
  @media (max-width: 900px) {
    .cond-grid {
      grid-template-columns: 1fr;
    }
  }
---

<div class="callout">
<strong>Pre-print</strong>
<a href="https://arxiv.org/abs/2602.13483">Finding Highly Interpretable Prompt-Specific Circuits in Language Models</a>
</div>

This note summarizes Appendix B of the paper above and gives a geometric intuition for handling QK bias and RoPE using a single bilinear form.

## 1. QK attention as a bilinear map

For one attention head, the pre-Softmax score between destination token $d$ and source token $s$ is defined as

$$
A'_{ds} = x_d^\top \Omega x_s, \qquad \Omega = W_Q W_K^\top.
$$

So QK analysis is fundamentally a bilinear map: destination-side vectors are matched against source-side vectors through $\Omega$.
Using SVD,

$$
\Omega = \sum_{k=1}^{R} u_k \sigma_k v_k^\top,
$$

gives paired directions $(u_k, v_k)$ that define candidate communication channels.

## 2. Related work on SVD of QK

A growing line of work studies QK structure in singular-vector coordinates and shows that this basis captures interpretable communication structure.

Pan et al. analyze query-key interaction in vision transformers through spectral structure, showing that singular directions provide a useful lens for understanding attention behavior <d-cite key="NEURIPS2024_6216515a"></d-cite>.
Merullo et al. study inter-layer communication in language transformers and similarly motivate analyzing how structured directions are transmitted and read across layers <d-cite key="merullo2024talkingheadsunderstandinginterlayer"></d-cite>.
Franco and Crovella introduce sparse attention decomposition, explicitly using QK singular vectors to isolate low-dimensional attention-relevant signal components for circuit tracing <d-cite key="franco2024sparseattentiondecompositionapplied"></d-cite>.

This post builds on that perspective and focuses on a practical extension: keeping one fixed bilinear core even when attention includes bias and/or RoPE terms.

## 3. Why bias and position terms make QK analysis harder

In practice, many models do not use the plain form $x_d^\top \Omega x_s$:

- bias models add query/key bias terms,
- RoPE models apply position-dependent rotations,
- some models do both.

If handled naively, this introduces either homogeneous-coordinate bookkeeping or position-specific $\Omega$ matrices, which complicates implementation and interpretation.

The Appendix B goal is to keep a single fixed $\Omega$ per head and absorb bias/position effects into transformed token vectors.

## 4. Bias: translate first, then project

For bias models,

$$
A'_{ds} = (x_d^\top W_Q + b_Q^\top)(x_s^\top W_K + b_K)^\top.
$$

Under the (empirically supported) well-conditioning assumptions on $W_Q$ and $W_K$, we can define bias-derived offsets
$c_d, c_s$ through pseudoinverse mappings (e.g., $c_d^\top = b_Q^\top W_Q^{\dagger}$, similarly for $c_s$) and rewrite:

$$
A'_{ds} = (x_d^\top + c_d^\top)\,\Omega\,(x_s + c_s).
$$

As a concrete toy illustration, the figure uses a map $P:\mathbb{R}^3\to\mathbb{R}^2$ as an analogue of the Q/K projection.
Read the two rows as two paths:

- Top row (light red): $y_A=Px+\alpha b$ (project, then translate in low dimension).
- Bottom row (light blue): $y_B=P(x+\alpha c)$ with $c=P^\dagger b$ (translate in high dimension, then project).

The right panel compares the endpoints, showing the same commutation pattern used in the attention derivation.

<div class="l-page">
  <iframe src="{{ '/assets/plotly/bias-geometric-pipeline.html' | relative_url }}" frameborder="0" scrolling="no" height="660px" width="100%" style="border: 1px solid #ddd; background: #fff;"></iframe>
</div>

## 5. RoPE: rotate first, then project

For RoPE models, scores involve position rotations $R_d, R_s$, often written as a position-dependent effective matrix.
Appendix B shows we can instead define token-space linear maps $M_d, M_s$ and keep a fixed
$\Omega = W_Q W_K^\top$:

$$
A'_{ds} = (x_d^\top M_d)\,\Omega\,(M_s x_s).
$$

Using the Appendix B.2 construction:

$$
M_d = W_Q R_d W_Q^{\dagger},
\qquad
M_s = (W_K^\top)^{\dagger} R_s^\top W_K^\top,
$$

which gives

$$
(x_d^\top M_d)\,\Omega\,(M_s x_s)
= x_d^\top W_Q R_d R_s^\top W_K^\top x_s
= x_d^\top W_Q R_{(d-s)} W_K^\top x_s.
$$

As a concrete toy illustration, the figure again uses a $\mathbb{R}^3\to\mathbb{R}^2$ setup.
Read the two rows as two paths:

- Top row (light red): $y_A=PR_3x$ (rotate in $\mathbb{R}^3$, then project).
- Bottom row (light blue): $y_B=R_2Px$ (project, then rotate in $\mathbb{R}^2$).

Here $R_3$ and $R_2$ use the same angle parameter $\theta$ (controlled by the slider). The right panel compares the endpoints.
This mirrors Appendix B: position effects are absorbed into transformed vectors while preserving a fixed core bilinear map.

<div class="l-page">
  <iframe src="{{ '/assets/plotly/rope-geometric-pipeline.html' | relative_url }}" frameborder="0" scrolling="no" height="660px" width="100%" style="border: 1px solid #ddd; background: #fff;"></iframe>
</div>

## 6. Appendix: condition numbers in practice

The derivations rely on $W_Q$ and $W_K$ being well-conditioned (full column rank, stable pseudoinverse behavior).
Appendix B.4 reports this holds for the studied models (condition numbers below 1000, usually much smaller), including GPT-2 small, Pythia-160M, and Gemma-2 2B. Below are the per-matrix plots converted from your PDF figures.

### GPT-2 small

<div class="cond-grid">
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/gpt2-small_W_Q_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_Q$ across layers and heads." %}
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/gpt2-small_W_K_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_K$ across layers and heads." %}
</div>

### Pythia-160M

<div class="cond-grid">
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/pythia-160m_W_Q_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_Q$ across layers and heads." %}
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/pythia-160m_W_K_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_K$ across layers and heads." %}
</div>

### Gemma-2 2B

<div class="cond-grid">
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/gemma-2-2b_W_Q_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_Q$ across layers and heads." %}
{% include figure.liquid loading="eager" path="assets/img/posts/qk-bias-rope/gemma-2-2b_W_K_condition_numbers.png" class="img-fluid rounded z-depth-1 qk-img-white" zoomable=true caption="Condition numbers of $W_K$ across layers and heads." %}
</div>

### Practical takeaway

With this reformulation, ACC++ can treat no-bias, bias-only, RoPE-only, and bias+RoPE models under one unified bilinear interface.
In code terms: one $\Omega$, one SVD per head, same downstream signal extraction/tracing logic.
