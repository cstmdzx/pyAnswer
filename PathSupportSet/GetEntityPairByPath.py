# -*-coding:UTF-8-*-

# 用来从dbpd_spo中选出非常要命的词对，
# 同时考虑了每个谓语的方向
'''
import MySQLdb
import pdb

import sys
sys.path.append('..')
from MySQLConn import mysql_conn_name

cur = mysql_conn_name('dbpd_spo')
'''

import sys
sys.path.append('..')
#from Lib.VirtuosoLib import query_sparql
#from Lib.VirtuosoLib import json_to_list
from Lib.FuncVirtuosoConn import get_query_results


def get_entity_pair_by_path(str_path):
    # 根据谓语路径，产生对应的词对
    # 输入为每个谓语路径，返回结果为对应词对的list
    # 这里没有记录每个path的对应的candidate，调用之前要搞一个
    list_sql_cmd = list()
    list_direct = list()
    words_pred_with_dir = str_path.split(']')
    int_temp_num = 0

    # shengcheng sparql
    str_param_previous = '?x0'
    #str_sparql_prefix = 'select ?sl,?ol '
    str_sparql_cmd = 'select ?sl,?ol where { '
    str_sparql_cmd += '?x0 <http://www.w3.org/2000/01/rdf-schema#label> ?sl . '
    for each_pred_with_dir in words_pred_with_dir:
        int_temp_num += 1
        if each_pred_with_dir == '': # zui hou yi ge ke neng shi kong de
            continue
        words = each_pred_with_dir.split('[')
        str_pred = words[0]
        str_pred = '<' + str_pred + '>'
        str_direct = words[1]
        # print str_pred
        # print str_direct
        if str_direct == 'f':
            str_sparql_cmd += str_param_previous + ' ' + str_pred + ' ' + '?x' + str(int_temp_num) + '. '
        else:
            str_sparql_cmd += '?x' + str(int_temp_num) + ' ' + str_pred + ' ' + str_param_previous + '. '
        str_param_previous = '?x' + str(int_temp_num)
    str_sparql_cmd += str_param_previous + ' <http://www.w3.org/2000/01/rdf-schema#label> ?ol . }'
    str_sparql_final = str_sparql_cmd
    # print str_sparql_final

    # exec
    # 两个待开发的函数，
    # json_query_res = query_sparql(str_sparql_final) # sparql 查询, 返回的是json结果
    # list_res = json_to_list(json_query_res) # json结果转换为list

    list_res = get_query_results(str_sparql_final)
    #list_res = list()
    return list_res

    # print str_sparql_final

'''
        str_sql_cmd = '(select Sub,Obj from SPO where Pred = ' + str_pred + ') as temp' + str(int_temp_num)

        list_sql_cmd.append([str_sql_cmd, str_direct, 'temp' + str(int_temp_num)])
        # 一共传递三个参数,index:  0.sql语句  1.这里谓语的方向  2.表格的temp名
'''


'''
    # pdb.set_trace()
    # 这里需要考虑下一次连接的时候，到底是主语还是宾语作为连接的条件
    list_previous = list_sql_cmd[0]
    del list_sql_cmd[0]
    str_sql_cmd_res = ''
    str_sql_cmd_res += list_previous[0]
    # str_origin = ''
    # str_target = ''

    if list_previous[1] == 'f':
        str_pre_origin = 'Sub'
        str_pre_target = 'Obj'
    else:
        str_pre_origin = 'Obj'
        str_pre_target = 'Sub'

    str_previous_tablename = ''
    str_cur_tablename = ''
    for each_sql_cmd in list_sql_cmd:
        int_temp_num += 1
        if each_sql_cmd[1] == 'f':
            str_cur_origin = str_previous_tablename + 'Sub'
            str_cur_target = str_previous_tablename + 'Obj'
        else:
            str_cur_origin = str_previous_tablename + 'Obj'
            str_cur_target = str_previous_tablename + 'Sub'

        str_select_item_origin = str_previous_tablename + str_pre_origin
        str_select_item_target = str_cur_tablename + str_cur_target
        str_on_item_target = str_previous_tablename + str_pre_target
        str_on_item_origin = str_cur_tablename + str_cur_origin


        str_sql_cmd_res = '(select ' +\
                list_previous[2] + '.' + str_select_item_origin + ' as ' +list_previous[2]+str_pre_origin + ',' +\
                each_sql_cmd[2] + '.' + str_select_item_target + 'as ' +each_sql_cmd[2]+str_cur_target +\
                ' from' +' (' + list_previous[0] + ' left outer join ' + each_sql_cmd[0] + \
                ' on ' + list_previous[2] + '.' + str_on_item_target + '=' + each_sql_cmd[2] + '.' + str_on_item_origin + ')) as ' +\
                'temp' + str(int_temp_num)
        # str_pre_origin = str_cur_origin
        str_previous_tablename = list_previous[2]
        str_cur_tablename = each_sql_cmd[2]
        str_pre_target = str_cur_target
        list_previous[0] = str_sql_cmd_res
        # list_previous[1] = # 好像没用了，因为有target和origin
        list_previous[2] = 'temp' + str(int_temp_num)

    print str_sql_cmd_res

    #if str_direct == 'f':
'''


if __name__ == '__main__':

    #get_entity_pair_by_path('pred1[f]pred2[b]pred3[f]pred4[b]')
    listRes = get_entity_pair_by_path('http://dbpedia.org/property/placeofburial[f]')
    print listRes


