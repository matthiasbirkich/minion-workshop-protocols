Hands-on MinION Workshop Protocols

This repository is a prototype for providing practical scientific workshop protocols using GitHub and Quarto.

It explores how existing printable laboratory handouts can be complemented by an interactive web-based version while retaining the original PDF format.

The target audience is researchers participating in hands-on molecular biology and MinION sequencing workshops. The platform is intended to support self-directed practical work and scientific discussion rather than formal assessment or testing.

Current prototype

The current prototype contains Sections 3–5 of an existing MinION workshop protocol:

* PCR product check with agarose gel electrophoresis
* PCR clean-up
* DNA quantification

The original PDF handout is included for comparison.

Interactive Quarto version

The Quarto website provides:

* step-by-step laboratory protocols;
* interactive checkboxes;
* personal note fields;
* direct links to external scientific tools and resources;
* access to the printable PDF handout; and
* a short introduction to GitHub Discussions.

Checkbox states and personal notes are stored locally in the user’s browser using localStorage.

They therefore remain available when the page is reopened on the same browser and device, but they are not uploaded to GitHub and are not synchronized between devices.

Scientific raw data and information requiring permanent documentation should not be stored in these note fields.

Workshop website

The rendered Quarto website is available at:

https://matthiasbirkich.github.io/minion-workshop-protocols/

Repository structure

minion-workshop-protocols/
│
├── index.qmd
├── github_discussions.qmd
├── Protocol.pdf
├── _quarto.yml
│
├── figures/
│   └── promega_biomath_qr.png
│
└── .github/
    └── workflows/
        └── publish.yml

GitHub Discussions

GitHub Discussions can be used for scientific exchange, methodological questions, troubleshooting, suggestions, and follow-up discussions between workshop participants and researchers.

Discussions are intended as a complement to the practical protocols and are not used for assessment.

GitHub + Quarto and Moodle

This repository is not intended to demonstrate a complete replacement for a Learning Management System such as Moodle.

Instead, it explores a complementary approach:

* Moodle may provide institutional course access, participant organization, and general workshop information.
* GitHub provides version control, transparent access to protocols, software, data resources, and scientific discussion.
* Quarto transforms the workshop material into an accessible web interface while retaining the possibility of printable documents.

This approach may be particularly useful for research-oriented workshops in which participants work independently with laboratory protocols, external scientific resources, software, and datasets.

Status

Prototype / proof of concept

The current repository contains only a small part of the complete workshop material and is intended to evaluate the workflow and user experience before further migration of existing protocols.
