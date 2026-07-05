---
layout: page
title: Learning from Label Proportions
description: Model selection and benchmarking for a weakly supervised setting where only bag-level label proportions are known.
img: assets/img/projects/llp-bags.png
importance: 3
category: weakly supervised learning
related_publications: true
---

Learning from Label Proportions (LLP) is a weakly supervised problem: you only know the proportion of labels within each group of items (a bag), and you want to recover the labels of the individual items.

In our KDD 2023 paper, we show that the dependence structure between bags, items, and labels defines distinct LLP variants, and that accounting for it leads to better model selection across a wide range of datasets and algorithms {% cite 10.1145/3580305.3599307 %}. In a follow-up pre-print, we build on this to generate variant-specific datasets and propose guidelines for benchmarking LLP methods fairly, and use them to run an extensive benchmark of well-known algorithms {% cite franco2023evaluating %}.

Code and datasets are available at [llp-variants-kdd](https://github.com/gaabrielfranco/llp-variants-kdd) and [llp-variants-datasets-benchmarks](https://github.com/gaabrielfranco/llp-variants-datasets-benchmarks).
