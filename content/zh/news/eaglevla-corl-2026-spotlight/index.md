---
title: EagleVLA入选CoRL 2026 Spotlight
subtitle: 我们被CoRL 2026接收的论文EagleVLA（原名Jetson-PI）入选Spotlight，入选比例低于5%。

# Summary for listings and search engines
summary: 我们被CoRL 2026接收的论文EagleVLA（原名Jetson-PI）入选Spotlight，入选比例低于5%。该工作通过前瞻对齐异步校正、基于置信度的调度与高度优化的端侧推理引擎，实现了高效的机载VLA推理。

# Date published
date: "2026-10-03T00:00:00+08:00"

# Date updated
lastmod: "2026-10-03T00:00:00+08:00"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true

tags:
- 会议
---

我们被CoRL 2026接收的论文[EagleVLA（原名Jetson-PI）——Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/pdf/2607.12659)入选Spotlight，**入选比例低于5%**。EagleVLA针对低功耗机载设备上部署视觉-语言-动作（VLA）模型时推理延迟高、控制频率低的问题，提出轻量级未来校正模块，根据已提交执行的动作预测未来环境表征，使动作预测与实际执行时的环境状态对齐；同时，基于置信度的调度器自适应平衡视觉语言模型与动作专家的调用频率，并通过基于llama.cpp的推理引擎、CUDA图复用、GPU驻留中间缓冲和流程展开等系统优化加速端侧部署。在NVIDIA Jetson Orin上，该系统的控制频率相比原生PyTorch和vla.cpp分别提升8.66倍和5.41倍，并在LIBERO基准上取得比VLASH高14.8%的平均成功率。该工作由博士生Zebin Yang主导。
