---
title: "Practical public PUF enabled by solving max-flow problem on chip"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Jin Miao
- Kai Zhong
- David Z Pan

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2016-06-05T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2016-06-05T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *ACM/IEEE Design Automation Conference (DAC)*
publication_short: In *ACM/IEEE Design Automation Conference (DAC) 2016*

abstract: The execution-simulation gap (ESG) is a fundamental property of public physical unclonable function (PPUF), which exploits the time gap between direct IC execution and computer simulation. ESG needs to consider both advanced computing scheme, including parallel and approximate computing scheme, and IC physical realization. In this paper, we propose a novel PPUF design, whose execution is equivalent to solving the hard-to-parallel and hard-toapproximate max-flow problem in a complete graph on chip. Thus, max-flow problem can be used as the simulation model to bound the ESG rigorously. To enable an efficient physical realization, we propose a crossbar structure and adopt source degeneration technique to map the graph topology on chip. The di↵erence on asymptotic scaling between execution delay and simulation time is examined in the experimental results. The measurability of output difference is also verified to prove the physical practicality.

# Summary. An optional shortened abstract.
# summary: 

tags: 
- Hardware Security

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://ieeexplore.ieee.org/abstract/document/7544405'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ""
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
# - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
