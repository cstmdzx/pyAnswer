# -*-coding:UTF-8-*-

# 用来根据输入的词对选出path，考虑path的长度以及方向
import sys
sys.path.append('..')

from itertools import product
from Lib.FuncVirtuosoConn import get_query_results


def get_sparql_by_len(str_sub, str_obj, int_len):
    list_basic = ['[f]', '[b]']
    list_dir = list(product(list_basic, repeat=int_len))
    list_sparql = list()
    for each_tuple_dir in list_dir:
        str_sparql = ' where { ?x1 <http://www.w3.org/2000/01/rdf-schema#label> ' + str_sub + ' . '
        int_flag = 1
        str_pred = ''
        for each_dir in each_tuple_dir:

            if each_dir == '[f]':
                str_sparql += '?x' + str(int_flag) + ' ?p' + str(int_flag) + ' ?x' + str(int_flag + 1) + ' . '
            else:
                str_sparql += '?x' + str(int_flag + 1) + ' ?p' + str(int_flag) + ' ?x' + str(int_flag) + ' . '

            str_pred += ', ?p' + str(int_flag)

            int_flag += 1

        str_sparql += '?x' + str(int_flag) + ' <http://www.w3.org/2000/01/rdf-schema#label> ' + str_obj + ' . }'
        str_pred = str_pred[2:]
        #str_sparql = 'select ' + str_pred + str_sparql
        str_sparql = 'select ' + str_pred + str_sparql
        #print each_tuple_dir
        #print str_sparql
        list_sparql.append((str_sparql, each_tuple_dir))
    return list_sparql

def get_uri_by_label(str_sub):
    str_sparql = 'select ?x where { ?x <http://www.w3.org/2000/01/rdf-schema#label> ' + str_sub + ' }'
    list_label = get_query_results(str_sparql)
    if list_label.__len__() == 0:
        return 'len0'
    for each_label in list_label:
        #print(not(each_label['x'].find('Category')))
        if each_label['x'].find('Category') == -1:
            return each_label['x']
    #print list_label
    return list_label[0]['x']




def get_sparql_by_len_with_label(str_sub, str_obj, int_len):
    str_uri_sub = get_uri_by_label(str_sub)
    if str_uri_sub == 'len0':
        return list()
    str_uri_obj = get_uri_by_label(str_obj)
    if str_uri_obj == 'len0':
        return list()

    list_basic = ['[f]', '[b]']
    list_dir = list(product(list_basic, repeat=int_len))
    list_sparql = list()
    for each_tuple_dir in list_dir:
        #str_sparql = ' where { ?x1 <http://www.w3.org/2000/01/rdf-schema#label> ' + str_sub + ' . '
        str_sparql = ' where { '
        int_flag = 1
        str_pred = ''
        for each_dir in each_tuple_dir:

            if each_dir == '[f]':
                str_sparql += '?x' + str(int_flag) + ' ?p' + str(int_flag) + ' ?x' + str(int_flag + 1) + ' . '
            else:
                str_sparql += '?x' + str(int_flag + 1) + ' ?p' + str(int_flag) + ' ?x' + str(int_flag) + ' . '

            str_pred += ', ?p' + str(int_flag)

            int_flag += 1

        #str_sparql += '?x' + str(int_flag) + ' <http://www.w3.org/2000/01/rdf-schema#label> ' + str_obj + ' . }'
        str_not_equal_type = ' != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>'
        str_sparql += 'FILTER ('
        for i in range(1, int_flag):
            if i > 1:
                str_sparql += ' and'
            str_sparql += ' ?p' + str(i) + str_not_equal_type

        str_sparql += ') }'
        str_pred = str_pred[2:]
        str_sparql = 'select ' + str_pred + str_sparql
        str_sparql = str_sparql.replace('?x1', '<' + str_uri_sub + '>')
        str_sparql = str_sparql.replace('?x' + str(int_flag), '<' + str_uri_obj + '>')
        #print each_tuple_dir
        #print str_sparql
        list_sparql.append((str_sparql, each_tuple_dir))
    return list_sparql



if __name__ == '__main__':

    #listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 1)
    #strSparqlCmd, tupleDir = listSparql[0]
    #print tupleDir
    #print strSparqlCmd

    #listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 2)
    #strSparqlCmd, tupleDir = listSparql[0]
    #print tupleDir
    #print strSparqlCmd

    #listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 3)
    #strSparqlCmd, tupleDir = listSparql[0]
    #print tupleDir
    #print strSparqlCmd

    listSparql = get_sparql_by_len_with_label('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 3)
    strSparqlCmd, tupleDir = listSparql[0]
    print tupleDir
    print strSparqlCmd
