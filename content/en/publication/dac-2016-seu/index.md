---
title: "A monte carlo simulation flow for seu analysis of sequential circuits"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Ye Wang
- Michael Orshansky

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

abstract: "An efficient methodology for soft error analysis of sequential circuits based on Monte Carlo sampling is proposed. It uses nested sampling for faster statistical convergence: it samples only from the workload space and statically evaluates the conditional probability over the subspace of particle strike and circuit parameters. A novel check on the stationarity of machine state sequence to reduce the number of samples to convergence is introduced. The flow combines logic simulation for latch-level error propagation and stationarity diagnostic and an improved combinational error simulator with a new masking model based on signal controllability. Experiments show that nested sampling reduces the number of samples by up to 1500X and runtime by up to 25X compared to direct sampling. Stationarity checking allows reducing sampling number by 25%, on average. The new latching window model permits accuracy of within 1% from SPICE, compared to a 12% error with a prior model."

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

url_pdf: 'https://dl.acm.org/doi/abs/10.1145/2897937.2897967'
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
