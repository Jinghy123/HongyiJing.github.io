---
permalink: /
title: "Peilin Cai's Personal Website"
excerpt: "Last Updated on Sept. 19th"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}
<h2 id="about">About</h2>

I am in my third semester of the M.S. in Computer Science program at the University of Southern California. I am a researcher focused on computer vision (CV), large language models (LLMs), and multimodal generation. At USC’s [Graphics & Vision Lab](https://usc-gvl.github.io/) (advisor: [Prof. Yue Wang](https://yuewang.xyz/)), my work centers on 3D reconstruction under sparse observations, controllable generative rendering, and embodied navigation. More broadly, I explore the intersection of generative models, world modeling, and embodied intelligence: how to build interactive, explorable, high-fidelity worlds from very small sets of real images; how to couple geometric priors with diffusion/autoregressive models to produce videos with temporal consistency and realism; and how to make these capabilities run reliably on edge and in-vehicle platforms.

I am also keenly interested in LLM reasoning and multimodal out-of-distribution (OOD) detection. If you are interested in collaborating, please feel free to reach out. My preferred email is [peilinca@usc.edu](peilinca@usc.edu)

<hr />

<h2 id="publications">Publications</h2>

<!-- New style rendering if publication categories are defined -->
{% for post in site.publications reversed %}
  {% include archive-single-publication.html %}
{% endfor %}

<hr />

{% comment %}
Talks, Teaching, Portfolio, and Blog sections temporarily disabled.
{% endcomment %}

<h2 id="cv">CV</h2>
{% capture cv_md %}
### Education

- M.S. in University of Southern California, 2024-2026
- B.S. in Wuhan Univeristy, 2020-2024

### Work experience

- 2024.11-2025.05: Research Assistant
  - Fortis Lab, USC
  - Supervisor: Yue Zhao, Assistant Professor of USC
  - Research: Multimodal OOD Detection, Large Language Model's ability on personalization

- 2025.05-Now: Research Assistant
  - GVL Lab, USC
  - Supervisor: Yue Wang, Assistant Professor of USC
  - Research: Computer Vision, 3D Reconstruction and Video Generation for Embodied Navigation

### Skills

- Python, C, C++
{% endcapture %}
{{ cv_md | markdownify }}

<h3 id="cv">Publications</h3>

<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>
  
{% comment %}
CV: Talks and Teaching lists disabled.
{% endcomment %}
  
<!-- ### Service and leadership -->
