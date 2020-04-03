from django.shortcuts import render
from rdflib import Graph
import rdflib

g = Graph()
g.parse("index/Immunization.owl")


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index:]
    return c


def index(request):
    qres = g.query(
        """
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix owl: <http://www.w3.org/2002/07/owl#>
            PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 

            SELECT DISTINCT ?vac ?label
                WHERE{ 
                    ?vac rdfs:subClassOf moyin:Vaccine;
                             rdfs:label ?label.
                } order by ?label """)
    result = []
    for row in qres:
        result.append({
            'vaccine': strip(row['vac']),
            'label': row['label'],
        })
    return render(request, 'index/index.html', {'result': result})


