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

I am a master student researcher focused on computer vision (CV), large language models (LLMs), and multimodal generation. At USC’s [Graphics & Vision Lab](https://usc-gvl.github.io/) (advisor: [Prof. Yue Wang](https://yuewang.xyz/)), my work centers on 3D reconstruction under sparse observations, controllable generative rendering, and embodied navigation. More broadly, I explore the intersection of generative models, world modeling, and embodied intelligence: how to build interactive, explorable, high-fidelity worlds from very small sets of real images; how to couple geometric priors with diffusion/autoregressive models to produce videos with temporal consistency and realism; and how to make these capabilities run reliably on edge and in-vehicle platforms.

Before this, I carried out two research projects of great personal significance at [Prof. Yue Zhao](https://viterbi-web.usc.edu/~yzhao010/index.html)’s [FORTIS Lab](https://viterbi-web.usc.edu/~yzhao010/lab): [SecDOOD (ICCV 2025 Poster)](https://caipeilin.com/SecDOOD/) and [PERSONABENCH (NeurIPS 2025 MTI-LLM Spotlight)](https://github.com/PERSONA-bench/PERSONA). The former proposed a secure on-device OOD detection framework that requires no gradient backpropagation, offering insights for deploying personalized large models on edge devices; the latter introduced the first benchmark for evaluating the personalization capabilities of LLMs in multi-turn conversational settings. I am deeply grateful to Prof. Yue Zhao and the senior PhD students in the lab for their support.

I have extensive experience in multimodal out-of-distribution (OOD) detection and in the training, deployment, and inference of LLMs, and I am also honing my research skills in computer vision and robotics at the GVL Lab. My primary research interests include **probing and analyzing the limitations of LLMs**, **embodied intelligence** and **visual generative models**. If you are interested in collaborating, please feel free to reach out. My preferred email is [peilinca@usc.edu](peilinca@usc.edu)

### Current State:
- In my third semester of the M.S. in Computer Science program at the University of Southern California. 
- Currently working on two projects that will be submitted for publication.
- Seeking PhD opportunities.


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
<div class="cv-button-group" style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0;">
  <a class="btn btn--primary btn--large" href="{{ '/CV/Peilin_Cai_CV_en.pdf' | relative_url }}" target="_blank" rel="noopener">English CV</a>
  <a class="btn btn--primary btn--large" href="{{ '/CV/Peilin_Cai_CV_cn.pdf' | relative_url }}" target="_blank" rel="noopener">中文简历</a>
</div>
  
<!-- ### Service and leadership -->
