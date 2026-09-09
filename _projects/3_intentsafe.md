---
layout: page
title: "IntentSafe-CN: Intent-Aware Safety Diagnosis"
description: A multi-layer benchmark for Chinese harmful-content detection.
importance: 3
category: research
img: /assets/img/publication_preview/intentsafe-figure-1.png
---

**IntentSafe-CN** augments Chinese content-safety datasets with intermediate cognitive annotations, including surface-form variants, targets, expressed emotion, and communicative intent. This makes it possible to analyze whether a model fails at pragmatic interpretation or at applying a safety rule.

I designed and executed experiments, analyzed the independent contribution of surface signals, context, and intent, trained a lightweight intent-recognition model with LoRA, and prepared the paper figures and analysis. The benchmark supports source-specific and unified evaluation while preserving the original tasks and labels.

The paper is submitted to AAAI 2027 and is currently under review. I contributed as a co-first author.

{% include figure.liquid path="/assets/img/publication_preview/intentsafe-figure-1.png" alt="Comparison of direct classification and multi-layer diagnostic detection in IntentSafe-CN" caption="Figure 1. IntentSafe-CN makes target, emotion, and intent explicit before the final safety judgment." %}
