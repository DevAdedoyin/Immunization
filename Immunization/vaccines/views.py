from django.shortcuts import render
from rdflib import Graph

g = Graph()
g.parse("./index/Immunization.owl")


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index:]
    return c


def chars(request, vaccine):
    ########################
    ##########BCG###########
    ########################
    if vaccine == 'BCG':
        BCG = g.query(
        """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                    WHERE{ 
                        ?age rdf:type moyin:Age_For_BCG.
                        ?age rdfs:label ?agelabel.
                        ?prevention rdf:type moyin:BCG_Disease_Prevention.
                        ?prevention rdfs:label ?preventionlabel.
                        ?dose rdf:type moyin:BCG_Dose. 
                        ?dose rdfs:label ?doselabel.
                        ?doses rdf:type moyin:BCG_Doses.
                        ?doses rdfs:label ?doseslabel.
                        ?roa rdf:type moyin:BCG_Route_Of_Administration.
                        ?roa rdfs:label ?roalabel.
                        ?site rdf:type moyin:BCG_Vaccination.
                        ?site rdfs:label ?sitelabel. 
                        
                    } """)
        result = []
        for row in BCG:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/bcg.html', {'result': result})

    ##############################
    ##########HEPATITIS###########
    ##############################
    elif vaccine == 'Hepatitis_B':
        Hepa = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Hepatitis_B.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Hepatitis_B_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Hepatitis_B_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Hepatitis_B_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Hepatitis_B_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Hepatitis_B_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in Hepa:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/hepa.html', {'result': result})

    ########################
    ##########IPV###########
    ########################
    elif vaccine == 'Inactivated_Polio_Vaccine':
        ipv = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_IPV.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:IPV_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:IPV_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:IPV_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:IPV_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:IPV_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in ipv:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/ipv.html', {'result': result})

    ###########################
    #########MEASLES###########
    ###########################
    elif vaccine == 'Measles':
        measles = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Measles.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Measles_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Measles_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Measles_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Measles_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Measles_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in measles:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/measles.html', {'result': result})

    ########################
    ##########OPV###########
    ########################
    elif vaccine == 'Oral_Polio_Vaccine':
        opv = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_OPV.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:OPV_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:OPV_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:OPV_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:OPV_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:OPV_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in opv:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/opv.html', {'result': result})

    ################################
    ##########PENTAVALENT###########
    ################################
    elif vaccine == 'Pentavalent':
        pent = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Pentavalent.
                            optional{?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Pentavalent_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Pentavalent_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Pentavalent_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Pentavalent_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Pentavalent_Vaccination.
                            ?site rdfs:label ?sitelabel.} 
    
                        } """)
        result = []
        for row in pent:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/pent.html', {'result': result})

    ########################
    ##########PCV###########
    ########################
    elif vaccine == 'Pneumococcal_Conjugate_Vaccine':
        pcv = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_PCV.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:PCV_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:PCV_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:PCV_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:PCV_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:PCV_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in pcv:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/pcv.html', {'result': result})

    #########################
    ##########ROTA###########
    #########################
    elif vaccine == 'Rota':
        rota = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Rota.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Rota_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Rota_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Rota_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Rota_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Rota_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in rota:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/rota.html', {'result': result})

    #########################
    ##########VITA###########
    #########################
    elif vaccine == 'Vitamin_A':
        vit = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Vitamin_A.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Vitamin_A_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Vitamin_A_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Vitamin_A_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Vitamin_A_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Vitamin_A_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in vit:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/vit.html', {'result': result})

    ################################
    ##########YELLOWFever###########
    ################################
    elif vaccine == 'Yellow_Fever':
        yf = g.query(
            """
                    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX moyin: <http://www.immunization.com/vaccine/moyin#> 
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
                    SELECT DISTINCT ?age ?agelabel ?prevention ?preventionlabel ?dose ?doselabel ?doses ?doseslabel ?roa ?roalabel ?vaccination ?doses ?doseslabel ?site ?sitelabel
                        WHERE{ 
                            ?age rdf:type moyin:Age_For_Yellow_Fever.
                            ?age rdfs:label ?agelabel.
                            ?prevention rdf:type moyin:Yellow_Fever_Disease_Prevention.
                            ?prevention rdfs:label ?preventionlabel.
                            ?dose rdf:type moyin:Yellow_Fever_Dose. 
                            ?dose rdfs:label ?doselabel.
                            ?doses rdf:type moyin:Yellow_Fever_Doses.
                            ?doses rdfs:label ?doseslabel.
                            ?roa rdf:type moyin:Yellow_Fever_Route_Of_Administration.
                            ?roa rdfs:label ?roalabel.
                            ?site rdf:type moyin:Yellow_Fever_Vaccination.
                            ?site rdfs:label ?sitelabel. 
    
                        } """)
        result = []
        for row in yf:
            result.append({
                'age': strip(row['age']),
                'agelabel': row['agelabel'],
                'prevention': strip(row['prevention']),
                'preventionlabel': row['preventionlabel'],
                'dose': strip(row['dose']),
                'doselabel': row['doselabel'],
                'doses': strip(row['doses']),
                'doseslabel': row['doseslabel'],
                'roa': strip(row['roa']),
                'roalabel': row['roalabel'],
                'site': strip(row['site']),
                'sitelabel': row['sitelabel'],
            })
        return render(request, 'vaccination/yf.html', {'result': result})
