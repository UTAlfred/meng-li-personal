---
title: "TimingSAT: Decamouflaging timing-based logic obfuscation"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Kaveh Shamsi
- Yier Jin
- David Z Pan

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2018-10-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2018-10-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE International Test Conference (ITC)*
publication_short: In *IEEE International Test Conference (ITC) 2018*

abstract: "In order to counter advanced reverse engineering techniques, various integrated circuit (IC) camouflaging methods are proposed to protect hardware intellectual property (IP) proactively. For example, a timing-based camouflaging strategy is developed recently representing a new class of parametric camouflaging strategies. Unlike traditional IC camouflaging techniques that directly hide the circuit functionality, the new parametric strategies obfuscate the circuit timing schemes, which in turn protects the circuit functionality and invalidates all the existing attacks. In this paper, we propose a SAT attack, named TimingSAT, to analyze the security of such timing-based camouflaging strategies. We demonstrate that with a proper transformation of the camouflaged netlist, traditional SAT attacks are still effective to decamouflage the new protection methods. The correctness of the resolved circuit functionality is formally proved. While a direct implementation of TimingSAT suffers from poor scalability, we propose a simplification procedure to significantly enhance the attack efficiency without sacrificing the correctness of the decamouflaged netlist. The efficiency and effectiveness of TimingSAT is validated with extensive experimental results."

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

url_pdf: 'https://ieeexplore.ieee.org/abstract/document/8027112'
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
