from django.shortcuts import render
from rdflib import Graph
import rdflib

g = Graph()
g.parse("index/Immunization.owl")


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index:]
    return c


def home(request):
    return render(request, 'search/search.html')


def search(request):
    userValue = request.GET.get('s')
    userstr = str(userValue).lower()
    query = g.query(
        """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 

            SELECT  ?value ?superclass ?superlabel
            WHERE {?subject moyin:diseasePrevention ?value.
            ?subject rdf:type ?subclass.
            ?subclass rdfs:subClassOf ?superclass.
             ?superclass rdfs:label ?superlabel} 
            """)
    result = []
    for row in query:
        result.append({
            'value': row['value'],
            'superclass': strip(row['superclass']),
            'superlabel': row['superlabel'],
        })
    return render(request, 'search/result.html', {'result': result, 'userstr': userstr})