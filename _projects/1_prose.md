---
layout: page
title: "PROSE: Semantic Reflection and Multi-Objective Prompt Evolution"
description: An LLM-based prompt optimizer for robust multimodal content moderation.
importance: 1
category: research
img: /assets/img/publication_preview/prose-framework.png
---

**PROSE** is a reflection-driven, multi-objective evolution engine for moderation prompts. It addresses the tendency of automatic prompt optimization to memorize bad cases instead of learning reusable decision principles.

The system treats semantic abstraction as an optimization signal alongside task performance. It combines Pareto-based selection, heterogeneous model pools, semantic reflection, logic rewriting, semantic crossover, and dynamic similarity penalties to preserve candidate diversity and improve held-out generalization.

I built the configuration-driven platform and its task adapters, concurrent evaluation and quality gates, SQLite experiment persistence, population isolation, lineage tracking, checkpoint recovery, and experiment dashboard. The platform has been integrated into 10+ moderation scenarios across 7 customers. The related paper was accepted to Findings of EMNLP 2026, and the first-inventor patent is published as CN121960463A.

Paper: [OpenReview](https://openreview.net/forum?id=zNdQjdh1Zg#discussion)

{% include figure.liquid path="/assets/img/publication_preview/prose-framework.png" alt="PROSE framework overview" caption="Figure 1. Overview of the PROSE semantic reflection and multi-objective evolution framework." %}
