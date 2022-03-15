---
title: "A Synergistic Framework for Hardware IP Privacy and Integrity Protection"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- David Z. Pan

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2018-08-15T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2018-08-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["5", "7"]

# Publication name and optional abbreviated publication name.
publication: In *Springer*
publication_short: In *Springer (2018)*

abstract: As the technology node scales down to 45nm and beyond, the significant increase in design complexity and cost propels the globalization of the $400-billion semiconductor industry. However, such globalization comes at a cost. Although it has helped to reduce the overall cost by the worldwide distribution of integrated circuit (IC) design, fabrication, and deployment, it also introduces ever-increasing intellectual property (IP) privacy and integrity infringement. Recently, primary violations, including hardware Trojan, reverse engineering, and fault attack, have been reported by leading semiconductor companies and resulted in billions of dollars loss annually. While hardware IP protection strategies are highly demanded, the re- searches were just initiated lately and still remain preliminary. Firstly, the lack of the mathematical abstractions for these IP violations makes it difficult to formally evaluate and guarantee the effectiveness of the protections. Secondly, the poor scalability and cost-effectiveness of the state-of-the-art protection strategies make them impractical for real-world applications. Moreover, the absence of a holistic IP protection further diminishes the chance to address these highly correlated IP violations which exploit physical clues throughout the whole IC design flow. The dissertation proposes a synergistic framework to help IP vendors to protect hardware IP privacy and integrity from design, optimization, and evaluation perspectives. The proposed framework consists of five interacting components that directly target at the primary IP violations. First, to prevent the insertion of the hardware Trojan, a split manufacturing strategy is proposed that achieves formal security guarantee while minimizes the introduced overhead. Then, to hinder reverse engineering, a fast security evaluation algorithm and a provably secure IC camouflaging strategy are proposed. Meanwhile, to impede the fault attacks, a new security primitive, named as public physical unclonable function (PPUF), is designed as an alternative to the existing cryptographic modules. A novel cross-level fault attack evaluation procedure also is proposed to help designers to identify security-critical components to protect general purpose processors and compare different security enhancement strategies against the fault attack. All the five algorithms are developed based on rigorous mathematical modeling for primary IP violations and focus on different stages of IC design, which can be combined synergistically to provide a formal security guarantee.

# Summary. An optional shortened abstract.
summary: Publised by Springer, UT Austin Margarida Jacome Outstanding Dis- sertation Prize, EDAA Outstanding Dissertation Award, ACM Student Research Competition Grand Final First Place

tags: 
- Hardware Security

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://link.springer.com/book/10.1007/978-3-030-41247-0'
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

# {{% callout note %}}
# Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
# {{% /callout %}}
 
# {{% callout note %}}
# Create your slides in Markdown - click the *Slides* button to check out the example.
# {{% /callout %}}
 
# Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/).

