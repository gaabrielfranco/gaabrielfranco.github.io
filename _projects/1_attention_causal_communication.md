---
layout: page
title: Attention-Causal Communication
description: Tracing circuits from a single forward pass by finding the low-dimensional signals that cause attention.
img: assets/img/posts/acc/fig3-graph-merged.png
importance: 1
category: interpretability
related_publications: true
---

Understanding *why* an attention head attends where it does is a central challenge in
mechanistic interpretability. This line of work introduces **attention-causal communication (ACC)**:
low-dimensional features that are written into and read from tokens, and that have a provable
causal relationship to attention patterns.

By identifying these signals, we can perform prompt-specific circuit discovery in a single forward
pass — without replacement models or activation patching {% cite franco2025pinpointing %}.
The follow-up method, **ACC++**, extracts cleaner, lower-dimensional causal signals and shows that
many of them are *interpretable*: a substantial portion admit a short natural-language description.
Applied to indirect object identification (IOI), ACC++ reveals that prompt-specific circuits form
well-defined clusters, and that across clusters heads receive systematically different signals
corresponding to distinct mechanisms {% cite franco2026finding %}.

The method is available as a pip-installable library:
[`accpp-tracer`](https://github.com/gaabrielfranco/accpp-tracer). Code to reproduce the papers is
at [pinpointing-attention-causal-communication](https://github.com/gaabrielfranco/pinpointing-attention-causal-communication)
and [finding-highly-interpretable-circuits](https://github.com/gaabrielfranco/finding-highly-interpretable-circuits).
