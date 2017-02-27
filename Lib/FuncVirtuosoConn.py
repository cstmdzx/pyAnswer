# -*-coding:UTF-8-*-

# connect to python use python

import urllib
import json
import time

def sparql_query(str_query, str_base_url='http://localhost:8890/sparql', str_format='application/sparql-results+json'):
    dict_params={
            'default-graph-uri': 'dbpedia',
            'query': str_query,
            'debug': 'on',
            'timeout': '',
            'format': str_format
            }

    str_query_part = urllib.urlencode(dict_params)
    str_query_url = str_base_url+'?'+str_query_part
    #print str_query_url
    response = urllib.urlopen(str_base_url+'?'+str_query_part).read()
    #print response
    return json.loads(response)

def get_query_results(str_query, str_base_url='http://localhost:8890/sparql', str_format='application/sparql-results+json'):
    dict_query_res = sparql_query(str_query)
    list_res = dict_query_res['results']['bindings']
    # print list_res
    list_res_return = list()
    for each_res in list_res:
        # each_res is a dict
        '''
        e.g.
        {
            'x': {'type': 'uri', 'value': 'http://dbpedia.org/property/accessDate'},
            'p': {'type': 'uri', 'value': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'}
        }
        '''
        dict_each_res = dict()
        for each_key in each_res:
            dict_each_res[each_key] = each_res[each_key]['value']
        list_res_return.append(dict_each_res)

    return list_res_return



# def

if __name__ == '__main__':
    #strQuery = 'select ?x,?p where {?x ?p ?o} limit 10'
    #strQuery = 'select ?x where {?x <http://www.w3.org/2000/01/rdf-schema#label> "Hawai\'i"@en} limit 10'
    #strQuery = 'select ?x where {?x ?p "AccessibleComputing"@en} limit 10'
    fileTestSparql = open('FileTestSparql')
    strQuery = fileTestSparql.readline()
    strQuery = strQuery.replace('\n', '')
    strQuery = '\"' + strQuery + '\"@en'

    strQuery = 'select ?x1,?x2 where {<http://dbpedia.org/resource/Hawai\'i> ?x1 ' + strQuery + ' . <http://dbpedia.org/resource/Hawai\'i> ?x2 ?c . } limit 10'
    start = time.clock()

    '''
    jsonRes = sparql_query(strQuery)
    print time.clock() - start
    print jsonRes
    print jsonRes['results']['bindings']
    listRes = jsonRes['results']['bindings']
    for eachDict in listRes:
        print eachDict['x']
    '''
    '''
        for eachDictKey in eachDict:
            print eachDict[eachDictKey]
        # print eachDict['x']['value']
    '''
    listRes = get_query_results(strQuery)
    print time.clock() - start
    print listRes
