---
# A filterable portfolio of recent publications.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 70

title: Recent Publications
subtitle: 'More detailed publication lists available through [Google Scholar](https://scholar.google.com/citations?user=lvdRkEkAAAAJ&hl=en)'

content:
  page_type: publication
  # Display all publications so filters apply to the complete collection.
  count: 0
  order: desc
  filter_default: 0
  filter_button:
  - name: All
    tag: '*'
  - name: Efficient AI
    tag: Efficient AI
  - name: Private AI
    tag: Private AI
  - name: Hardware
    tag: Hardware
  - name: Algorithm
    tag: Algorithm/Software

design:
  # Choose a view for the listings:
  view: citation
  columns: '1'
---
