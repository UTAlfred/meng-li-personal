---
title: EagleVLA Selected as a CoRL 2026 Spotlight
subtitle: Our CoRL 2026 paper EagleVLA, originally named Jetson-PI, has been selected as a spotlight, an honor awarded to fewer than 5% of accepted papers.

# Summary for listings and search engines
summary: Our paper EagleVLA (formerly Jetson-PI), accepted by CoRL 2026, has been selected as a spotlight, an honor awarded to fewer than 5% of accepted papers. It enables efficient onboard VLA inference through foresight-aligned asynchronous correction, confidence-based scheduling, and a highly optimized edge inference engine.

# Date published
date: "2026-10-03T00:00:00+08:00"

# Date updated
lastmod: "2026-10-03T00:00:00+08:00"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true

tags:
- Conference
---

Our CoRL 2026 paper [EagleVLA (formerly Jetson-PI): Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/pdf/2607.12659) has been selected as a spotlight, a distinction awarded to **fewer than 5% of accepted papers**. EagleVLA addresses the high latency and low control frequency of deploying vision-language-action models on low-power onboard devices by introducing a lightweight future-correction module that predicts future environment representations from committed actions, thereby aligning action predictions with the state of the environment at execution time; a confidence-based scheduler then adaptively balances vision-language model and action-expert invocations, while a llama.cpp-based inference engine accelerates deployment through CUDA graph reuse, GPU-resident intermediate buffering, and flow unrolling. On NVIDIA Jetson Orin, the system improves control frequency by 8.66× over naive PyTorch and 5.41× over vla.cpp, while achieving a 14.8% higher average success rate than VLASH on the LIBERO benchmark. This work is led by our PhD student Zebin Yang.
