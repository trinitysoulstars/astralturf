#!/usr/bin/env python
""" Make an index page where you can find datagrepper stuff. """

import jinja2
import arrow

corpus = {
        "Astral Seed": "https://trinitysoulstars.com",
        "Starseed": "https://trinitysoulstars.com",
        "Ascension Symptoms": "https://trinitysoulstars.com",
        "LightBody": "https://trinitysoulstars.com",
        "Manifest": "https://trinitysoulstars.com",
        "Dopeness": "https://trinitysoulstars.com",
        "Five Cars": "https://trinitysoulstars.com",
        "Juice Brew": "https://trinitysoulstars.com",
        "Guarav": "https://trinitysoulstars.com",
        "Theosyn": "https://trinitysoulstars.com",
        "Realms": "https://trinitysoulstars.com",
        "Higher": "https://trinitysoulstars.com",
        "Self": "https://trinitysoulstars.com",
        "TRS": "https://trinitysoulstars.com",
        "Bubblin": "https://trinitysoulstars.com",
        "Mt Meru": "https://trinitysoulstars.com",
        }

for term,link in corpus.iteritems():
    print term,link

template = jinja2.Template("""
<html> <body>


<h2>Corpus</h2>
    <div>
    <p>
        {% for term,link in corpus.iteritems(): %}
            <a target="_blank" href="{{link}}">{{term}}</a> 
        {% endfor %}
    </p>
    </div>

</body> </html>
""")

output = template.render(corpus=corpus)

with open('{}-cloud.html'.format(arrow.now().format()[0:10]), "wb") as f:
        f.write(output)
