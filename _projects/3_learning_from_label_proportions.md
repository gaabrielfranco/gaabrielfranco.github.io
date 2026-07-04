---
layout: page
title: Learning from Label Proportions
description: Model selection, dependence structure, and benchmarking for weakly supervised learning from bag-level label proportions.
importance: 3
category: weakly supervised learning
related_publications: true
---

In Learning from Label Proportions (LLP), a model that assigns labels to individual items is learned
using knowledge of only the *proportion* of labels within predefined groups, called bags. Despite its
many applications, LLP has several unusual aspects that complicate both learning and evaluation.

This work argues that a careful approach to model selection for LLP requires consideration of the
dependence structure that exists between bags, items, and labels. We formalize this structure, show how
it affects model selection, and derive improved methods that outperform the state of the art across a
wide range of datasets and LLP algorithms {% cite 10.1145/3580305.3599307 %}. Building on this, we
develop methods to generate variant-specific datasets, propose guidelines for benchmarking LLP
algorithms, and run an extensive benchmark showing that the best algorithm depends critically on the
LLP variant and the model selection method {% cite franco2023evaluating %}.

Code and datasets are available at
[llp-variants-kdd](https://github.com/gaabrielfranco/llp-variants-kdd) and
[llp-variants-datasets-benchmarks](https://github.com/gaabrielfranco/llp-variants-datasets-benchmarks).
