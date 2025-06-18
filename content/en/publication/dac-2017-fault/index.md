---
title: "Cross-level monte carlo framework for system vulnerability evaluation against fault attack"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Liangzhen Lai 
- Vikas Chandra
- David Z. Pan

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2017-06-18T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-06-18T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *ACM/IEEE Design Automation Conference (DAC)*
publication_short: In *ACM/IEEE Design Automation Conference (DAC) 2017*

abstract: "Fault attack becomes a serious threat to system security and requires to be evaluated in the design stage. Existing methods usually ignore the intrinsic uncertainty in attack process and suffer from low scalability. In this paper, we develop a general framework to evaluate system vulnerability against fault attack. A holistic model for fault injection is incorporated to capture the probabilistic nature of attack process. Based on the probabilistic model, a security metric named as System Security Factor (SSF) is defined to measure the system vulnerability. In the framework, a Monte Carlo method is leveraged to enable a feasible evaluation of SSF for different systems, security policies, and attack techniques. We enhance the framework with a novel system pre-characterization procedure, based on which an importance sampling strategy is proposed. Experimental results on a commercial processor demonstrate that compared to random sampling, a 2500X speedup is achieved with the proposed sampling strategy. Meanwhile, 3% registers are identified to contribute to more than 95% SSF. By hardening these registers, a 6.5X security improvement can be achieved with less than 2% area overhead."

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

url_pdf: 'https://ieeexplore.ieee.org/abstract/document/8060390'
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
