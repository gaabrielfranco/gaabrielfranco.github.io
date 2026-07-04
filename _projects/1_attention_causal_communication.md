---
layout: page
title: Understanding why an attention head attends where it does
description: Isolating the low-dimensional signals that cause attention, and using them to trace interpretable circuits from a single forward pass.
img: assets/img/posts/acc/fig3-graph-merged.png
importance: 1
category: interpretability
related_publications: true
---

Much of my research is about understanding why an attention head attends where it does. When a head attends from one token to another, I want to identify the specific information in the residual stream that caused that choice.

This line of work began with Sparse Attention Decomposition, where we showed that the signals attention heads use to communicate are often sparsely encoded in the singular vectors of their query-key matrices {% cite franco2024sparse %}. We developed that idea into attention-causal communication (ACC): a way to isolate those signals as low-dimensional features with a provable causal link to attention, and to trace circuits from a single forward pass. That paper was published at NeurIPS 2025 {% cite franco2025pinpointing %}.

More recently, ACC++ refines the method to extract cleaner, lower-dimensional signals, many of which admit a short natural-language description, and uses them to find interpretable prompt-specific circuits {% cite franco2026finding %}.

The method is available as a pip-installable library, [accpp-tracer](https://github.com/gaabrielfranco/accpp-tracer). Code for the individual papers lives in [sparse-attention-decomposition](https://github.com/gaabrielfranco/sparse-attention-decomposition), [pinpointing-attention-causal-communication](https://github.com/gaabrielfranco/pinpointing-attention-causal-communication), and [finding-highly-interpretable-circuits](https://github.com/gaabrielfranco/finding-highly-interpretable-circuits).
