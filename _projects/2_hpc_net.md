---
layout: page
title: "HPC-Net: Brain-Inspired Multimodal Emotion Recognition"
description: Isolating auxiliary supervision before target-conditioned multimodal integration.
importance: 2
category: research
img: /assets/img/publication_preview/hpc-net-figure-1.png
---

**HPC-Net** is a brain-inspired isolation-integration framework for robust multi-dataset multimodal emotion recognition. Heterogeneous affective-computing datasets differ in domains, tasks, and label semantics, so direct joint training can cause negative transfer.

The framework first trains auxiliary dataset-task branches independently. In the integration phase, frozen auxiliary encoders process target examples while a trainable target branch and retrieval modules receive target supervision. Gated representations, route-specific cross-attention, and a shared mixture-of-experts pool provide target-conditioned feature selection.

The work evaluates sentiment, emotion, and sarcasm tasks across CH-SIMSv2, MELD, and MUStARD. It is a first-author AAAI 2027 submission currently under review.

{% include figure.liquid path="/assets/img/publication_preview/hpc-net-figure-1.png" alt="Conceptual overview of the HPC-Net isolation-integration learning paradigm" caption="Figure 1. HPC-Net first isolates dataset-specific knowledge and then selectively integrates multi-source knowledge." %}
