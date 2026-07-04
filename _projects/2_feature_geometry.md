---
layout: page
title: Feature Geometry in Attention Heads
description: When and why the singular vectors of attention matrices align with the features a model uses.
img: assets/img/posts/acc/fig1-distribution-merged.png
importance: 2
category: interpretability
related_publications: true
---

Identifying feature representations is a central task in mechanistic interpretability. Several studies
have observed that feature representations can sometimes be inferred from the singular vectors of
attention matrices — but sound justification for this phenomenon was lacking.

This work asks: *why and when do singular vectors align with features?* We first demonstrate that
singular vectors robustly align with features in a model where features can be directly observed, and
then show theoretically that such alignment is expected under a range of conditions
{% cite franco2026singular %}. Operationally, we identify **sparse attention decomposition** as a
testable prediction of this alignment, and show that it emerges in real models such as GPT-2 small
when tracing the circuits used for the indirect object identification (IOI) task
{% cite franco2024sparse %}.

Code is available at [svf-alignment](https://github.com/gaabrielfranco/svf-alignment) and
[sparse-attention-decomposition](https://github.com/gaabrielfranco/sparse-attention-decomposition).
