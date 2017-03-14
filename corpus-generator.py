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

terms=[]

for term,link in corpus.iteritems():
    print term,link
    terms.append(term)

print terms



template = jinja2.Template("""
<html>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>RemyD @ RIT</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8"/>
    <meta http-equiv="Content-Style-Type" content="text/css"/>
    <meta name="description" content="Hacktivist & Storyteller -  />
    <meta name="keywords" content="
        {%- for term in terms: -%}
            {{term}},
        {%- endfor %}"/>
    <meta name="author" content="decause, FLOSSOpher - Trinity Soulstars - https://github.com/trinitysoulstars"/>
    <link rel="stylesheet" type="text/css" href="style.css" media="screen"/>
    <link href="favicon.ico rel=" shortcut icon" />
</head>

<style>
<body>



<h2>Corpus</h2>
    <div>
    <p>
        {% for term,link in corpus.iteritems(): %}
            <a target="_blank" href="{{link}}">{{term}}</a> 
        {% endfor %}
    </p>
    </div>

</body>
</html>
""")

output = template.render(corpus=corpus,terms=terms)

with open('{}-cloud.html'.format(arrow.now().format()[0:10]), "wb") as f:
        f.write(output)
