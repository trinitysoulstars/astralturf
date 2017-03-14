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
titles = ["AstralTurf: Protonode"]
metadesc = ["AstralTurn: Protonode Description Goes Here"]
authors = ["decause, FLOSSOpher - Trinity Soulstars - https://github.com/trinitysoulstars"]

for term,link in corpus.iteritems():
    print term,link
    terms.append(term)

print "terms =  %s " % terms
print "titles = %s " % titles
print "metadesc = %s " % metadesc
print "authors = %s " % authors



template = jinja2.Template("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>
        {%- for title in titles: -%}
            {{title}}
        {%- endfor -%}
        </title>

    <meta name="description" content="
        {%- for desc in metadesc: -%}
            {{desc}}
        {%- endfor -%}"/>

    <meta name="keywords" content="
        {%- for term in terms: -%}
            {{term}},
        {%- endfor %}"/>

    <meta name="author" content="
        {%- for author in authors: -%}
            {{author}}
        {%- endfor -%}"/>
    <link rel="stylesheet" type="text/css" href="style.css" media="screen"/>
    <link href="favicon.ico rel=" shortcut icon" />
</head>

<body>



<h2>Corpus</h2>
    <div id='cloud'>
    <p>
        {% for term,link in corpus.iteritems(): %}
            <a target="_blank" href="{{link}}">{{term}}</a> 
        {% endfor %}
    </p>
    </div>

</body>
</html>
""")

output = template.render(corpus=corpus,terms=terms,titles=titles,metadesc=metadesc,authors=authors)

with open('{}-cloud.html'.format(arrow.now().format()[0:10]), "wb") as f:
        f.write(output)
