---
layout: page
title: Feature Geometry in Attention Heads
description: When and why the singular vectors of attention matrices align with the features a model uses.
img: assets/img/projects/svf-geometry.png
importance: 2
category: interpretability
related_publications: true
---

Several studies have noticed that you can often read a model's features off the singular vectors of its attention matrices (including [my own work]({{ '/projects/1_attention_causal_communication/' | relative_url }})), but it was not clear why this happens. In this ICML 2026 paper, we give an answer {% cite franco2026singular %}. We first show that singular vectors reliably align with features in a setting where the features can be observed directly, and then prove that this alignment is expected under a range of conditions. We also identify sparse attention decomposition as a testable signature of the alignment and find it in real models.

{% include figure.liquid loading="eager" path="assets/img/projects/svf-cosine-alignment.png" class="img-fluid rounded z-depth-1" zoomable=true caption="In a controlled setting, the singular vectors of an attention head come to align with the model's features over the course of training." %}

Code is available at [svf-alignment](https://github.com/gaabrielfranco/svf-alignment).
