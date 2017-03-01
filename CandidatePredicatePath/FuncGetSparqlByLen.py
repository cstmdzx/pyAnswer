# -*-coding:UTF-8-*-

# 用来根据输入的词对选出path，考虑path的长度以及方向
from itertools import product


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


if __name__ == '__main__':
    listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 1)
    strSparqlCmd, tupleDir = listSparql[0]
    print tupleDir
    print strSparqlCmd

    listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 2)
    strSparqlCmd, tupleDir = listSparql[0]
    print tupleDir
    print strSparqlCmd

    listSparql = get_sparql_by_len('"Saint Mary Parish, Jamaica"@en', '"Portland Parish"@en', 3)
    strSparqlCmd, tupleDir = listSparql[0]
    print tupleDir
    print strSparqlCmd
