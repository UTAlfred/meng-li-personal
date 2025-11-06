---
title: 'MPCache: MPC-Friendly KV Cache Eviction for Efficient Private LLM Inference'
summary: Based on the Secretflow project developed by Ant Group, develop the first model/protocol co-optimization framework for static-dynamic sparse attention in LLM.

tags:
- Deep Learning
date: "2025-11-01T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

# image:
#   caption: Photo by rawpixel on Unsplash
#   focal_point: Smart

links:
# - icon: twitter
#   icon_pack: fab
#   name: Follow
#   url: https://twitter.com/georgecushen
url_code: https://github.com/PKU-SEC-Lab/MPCache
url_pdf: https://arxiv.org/abs/2501.06807
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Neural architecture search (NAS) has shown great promise in designing state-of-the-art (SOTA) models that are both accurate and efficient. Recently, two-stage NAS, e.g. BigNAS, decouples the model training and searching process and achieves remarkable search efficiency and accuracy. Two-stage NAS requires sampling from the search space during training, which directly impacts the accuracy of the final searched models. While uniform sampling has been widely used for its simplicity, it is agnostic of the model performance Pareto front, which is the main focus in the search process, and thus, misses opportunities to further improve the model accuracy. In this work, we propose AttentiveNAS that focuses on improving the sampling strategy to achieve better performance Pareto. We also propose algorithms to efficiently and effectively identify the networks on the Pareto during training. Without extra re-training or post-processing, we can simultaneously obtain a large number of networks across a wide range of FLOPs. Our discovered model family, AttentiveNAS models, achieves top-1 accuracy from 77.3% to 80.7% on ImageNet, and outperforms SOTA models, including BigNAS and Once-for-All networks. We also achieve ImageNet accuracy of 80.1% with only 491 MFLOPs.

