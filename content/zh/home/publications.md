---
# A filterable portfolio of recent publications.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 70

title: 近期论文
subtitle: '完整论文列表请访问 [Google Scholar](https://scholar.google.com/citations?user=lvdRkEkAAAAJ&hl=en)'

content:
  page_type: publication
  # Display all publications so filters apply to the complete collection.
  count: 0
  order: desc
  filter_default: 0
  filter_button:
  - name: 全部
    tag: '*'
  - name: 高效人工智能
    tag: Efficient AI
  - name: 隐私保护人工智能
    tag: Private AI
  - name: 硬件
    tag: Hardware
  - name: 算法
    tag: Algorithm/Software

design:
  # Choose a view for the listings:
  view: citation
  columns: '1'
---
