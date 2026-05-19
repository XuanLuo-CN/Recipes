---
layout: default
title: About
permalink: /about/
---

<div class="prose max-w-3xl mx-auto px-6 py-12">
  {% capture readme %}{% include_relative README.md %}{% endcapture %}
  {{ readme | markdownify }}
</div>
