---
permalink: /
title: "Sailing To Linux"
excerpt: "Last Updated on Sept. 19th"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}
<span id="about"></span>
## About

I am in my third semester of the M.S. in Computer Science program at the University of Southern California. I am a researcher focused on computer vision (CV), large language models (LLMs), and multimodal generation. At USC’s [Graphics & Vision Lab](https://usc-gvl.github.io/) (advisor: [Prof. Yue Wang](https://yuewang.xyz/)), my work centers on 3D reconstruction under sparse observations, controllable generative rendering, and embodied navigation. More broadly, I explore the intersection of generative models, world modeling, and embodied intelligence: how to build interactive, explorable, high-fidelity worlds from very small sets of real images; how to couple geometric priors with diffusion/autoregressive models to produce videos with temporal consistency and realism; and how to make these capabilities run reliably on edge and in-vehicle platforms.

I am also keenly interested in LLM reasoning and multimodal out-of-distribution (OOD) detection. If you are interested in collaborating, please feel free to reach out. My preferred email is [peilinca@usc.edu](peilinca@usc.edu)

<hr />

<span id="publications"></span>
## Publications

<!-- New style rendering if publication categories are defined -->
{% for post in site.publications reversed %}
  {% include archive-single-publication.html %}
{% endfor %}

<hr />

<span id="talks"></span>
## Talks and presentations

{% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>

{% endif %}

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}

<hr />

<span id="teaching"></span>
## Teaching

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}

<hr />

<span id="portfolio"></span>
## Portfolio

{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}

<hr />

<span id="blog"></span>
## Blog Posts

{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

<hr />

<span id="cv"></span>
## CV

Education
======
* Ph.D in Version Control Theory, GitHub University, 2018 (expected)
* M.S. in Jekyll, GitHub University, 2014
* B.S. in GitHub, GitHub University, 2012

Work experience
======
* Spring 2024: Academic Pages Collaborator
  * GitHub University
  * Duties includes: Updates and improvements to template
  * Supervisor: The Users

* Fall 2015: Research Assistant
  * GitHub University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub

* Summer 2015: Research Assistant
  * GitHub University
  * Duties included: Tagging issues
  * Supervisor: Professor Git
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
