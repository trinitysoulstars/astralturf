# astralturf

## Overview

The idea is to create an ecosystem of static sites that are fractally
self-referential to improve SEO results, and stake claim on the unique
linguistic corpus of the TSS brand.

By having each static site use <code><meta></code> tags, that refer to the
corpus and other sites in the ecosystem, and having those names link to each
other site in the ecosystem, you create a dense mesh that should improve
presence and results.

By using a simple static site generator, it should be trivial to set up a
singularly branded static template that will make it easy to crank out these
microsites by adding to the <code>corpus</code>.


Things we need:

- TSS Corpus
- Wireframe for base template


## Instructions

- create a python virtualenv (this is a multistep process)
- <code>$ pip install requirements.txt</code>
- <code>$ python corpus-generator.py</code>

This generates a time-stamped version of the HTML file (i.e. 2017-03-14-cloud.html)
To change the "demo" page seen at http://trinitysoulstars.github.io/astralturf, just copy this new file to <code>index.html</code>
