---
layout: page
title: "NeuroSIFT: Signal-Noise Separation for Multimodal Emotion Recognition"
description: A biologically inspired framework for robust multimodal emotion recognition.
importance: 4
category: research
img: /assets/img/publication_preview/neurosift-architecture.png
---

**NeuroSIFT** explicitly separates emotional signals from structured noise in multimodal inputs. Inspired by selective inhibition in hippocampal-prefrontal circuits, it uses a semantic-mimicry noise generator to create aligned noise references and a selective-inhibition module to decompose raw inputs.

The separated streams are trained with a dual-stream adversarial objective: purified signals support emotion classification, while suppressed noise patterns improve robustness. Experiments across multiple multimodal emotion-recognition benchmarks report up to a 5.44% F1 improvement on CH-SIMSv2.

The paper was accepted to ICASSP 2026 as a first-author work.

Paper: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11461551/)

{% include figure.liquid path="/assets/img/publication_preview/neurosift-architecture.png" alt="NeuroSIFT signal-noise separation architecture" caption="Figure 1. NeuroSIFT explicitly separates clean emotional signals from structured multimodal noise." %}
