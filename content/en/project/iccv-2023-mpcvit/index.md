---
title: 'MPCViT: Searching for Accurate and Efficient MPC-friendly Vision Transformer with Heterogeneous Attention'
summary: Develop MPCViT that leverages neural architecture search to search MPC-friendly vision transformers.
tags:
- Private Deep Learning

date: "2023-09-24T00:00:00Z"

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
url_code: https://https://github.com/PKU-SEC-Lab/mpcvit
url_pdf: https://arxiv.org/abs/2211.13955
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Secure multi-party computation (MPC) enables computation directly on encrypted data and protects both data and model privacy in deep learning inference. However, existing neural network architectures, including Vision Transformers (ViTs), are not designed or optimized for MPC and incur significant latency overhead. We observe Softmax accounts for the major latency bottleneck due to a high communication complexity, but can be selectively replaced or linearized without compromising the model accuracy. Hence, in this paper, we propose an MPC-friendly ViT, dubbed MPCViT, to enable accurate yet efficient ViT inference in MPC. Based on a systematic latency and accuracy evaluation of the Softmax attention and other attention variants, we propose a heterogeneous attention optimization space. We also develop a simple yet effective MPC-aware neural architecture search algorithm for fast Pareto optimization. To further boost the inference efficiency, we propose MPCViT+, to jointly optimize the Softmax attention and other network components, including GeLU, matrix multiplication, etc. With extensive experiments, we demonstrate that MPCViT achieves 1.9%, 1.3% and 3.6% higher accuracy with 6.2x, 2.9x and 1.9x latency reduction compared with baseline ViT, MPCFormer and THE-X on the Tiny-ImageNet dataset, respectively. MPCViT+ further achieves a better Pareto front compared with MPCViT. 
