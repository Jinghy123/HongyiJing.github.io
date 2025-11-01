---
permalink: /
title: "Hongyi Jing's Personal Website"
excerpt: "Last Updated on Oct. 30th"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}
<h2 id="about">About</h2>

I am a second-year CS master student at [University of Southern California](https://www.cs.usc.edu/), working with [Prof. Yue Wang](https://yuewang.xyz/) at [Graphics & Vision Lab](https://usc-gvl.github.io/). My research mainly focuses on Robotics, particularly **humanoid dexterous manipulation** and **whole-body control**. I aim to develop intelligent systems that enable humanoid robots to perform coordinated, dynamic, and physically interactive tasks in the real world.

Before this, I received my Bachelor's degree at [Huazhong University of Science and Technology](https://english.hust.edu.cn/), where I worked with [Prof. Xiang Xiang](https://eglxiang.github.io/). I also served as an research intern in [MINE Lab](https://sites.nd.edu/xiangliang-zhang/) led by [Prof.Xiangliang Zhang](https://engineering.nd.edu/faculty/xiangliang-zhang/) at [Notre Dame](https://cse.nd.edu/) during my senior year.

I am looking for Fall 2026 PhD opportunities and open to discuss potential research collaborations. Please contact me if you're interested!


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
  <a class="btn btn--primary btn--large" href="{{ '/CV/CV_HongyiJing.pdf' | relative_url }}" target="_blank" rel="noopener">CV</a>
</div>
  
<!-- ### Service and leadership -->
