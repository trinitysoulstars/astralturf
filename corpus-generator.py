#!/usr/bin/env python
""" Generate The Corpus Cloud with Page Elements, to be Styled """

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
videos = ['<iframe width="560" height="315" src="https://www.youtube.com/embed/lRQGn1f5pYQ" frameborder="0" allowfullscreen></iframe>']

for term,link in corpus.iteritems():
    print term,link
    terms.append(term)

print "terms =  %s " % terms
print "titles = %s " % titles
print "metadesc = %s " % metadesc
print "authors = %s " % authors
print "videos = %s " % videos



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
    <!-- Latest compiled and minified CSS --> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
</head>

<body>

<div class='container-fluid' id='cloud'>
<p>
    {% for term,link in corpus.iteritems(): %}
        <a target="_blank" href="{{link}}">{{term}}</a> 
    {% endfor %}
</p>
</div>

<div id='video'>
    {% for video in videos: %}
        {{video}},
    {% endfor %}"/>
</div>

</body>
</html>
""")

# When you add new elements to the template, you must define it outside the template, and then pass in the value below
output = template.render(corpus=corpus,terms=terms,titles=titles,metadesc=metadesc,authors=authors,videos=videos)

with open('{}-cloud.html'.format(arrow.now().format()[0:10]), "wb") as f:
        f.write(output)
