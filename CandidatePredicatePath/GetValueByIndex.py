# -*-coding:UTF-8-*-

# 用来从数据库中根据索引值选出对应值
# 主要包括根据S选OP，根据O选SP，根据P选SO
# 以及反过来

import MySQLdb
import time

import sys
sys.path.append('..')
from MySQLConn import mysql_conn

# conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
# cur = conn.cursor()
cur = mysql_conn()

def tuple_res_raw_to_list(tuple_raw):
    list_res = list()
    for each_tuple in tuple_raw:
        list_res.append(each_tuple[0])

    return list_res

def get_OP_by_S(int_Sub):
    str_sql_cmd = 'select ObjPred from S_OP where Sub=' + str(int_Sub)
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_ObjPred_raw = cur.fetchall()
    list_ObjPred = tuple_res_raw_to_list(tuple_ObjPred_raw)

    # 由于每一个都是tuple，因此返回所有tuple的第一个
    # return tuple_ObjPred_raw[:][0]
    return list_ObjPred

def get_SP_by_O(int_Obj):
    str_sql_cmd = 'select SubPred from O_SP where Obj=' + str(int_Obj)
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_SubPred_raw = cur.fetchall()
    #
    list_SubPred = tuple_res_raw_to_list(tuple_SubPred_raw)
    return list_SubPred

def get_SO_by_P(int_Pred):
    str_sql_cmd = 'select SubObj from P_SO where Pred=' + str(int_Pred)
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_SubObj_raw = cur.fetchall()
    #
    list_SubObj = tuple_res_raw_to_list(tuple_SubObj_raw)
    return list_SubObj


def get_S_by_OP(str_ObjPred):
    str_sql_cmd = 'select Sub from S_OP where ObjPred=\'' + str_ObjPred + '\''
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_Sub_raw = cur.fetchall()
    #
    list_Sub = tuple_res_raw_to_list(tuple_Sub_raw)
    return list_Sub


def get_O_by_SP(str_SubPred):
    str_sql_cmd = 'select Obj from O_SP where SubPred=\'' + str_SubPred + '\''
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_Obj_raw = cur.fetchall()
    #
    list_Obj = tuple_res_raw_to_list(tuple_Obj_raw)
    return list_Obj

def get_P_by_SO(str_SubObj):
    str_sql_cmd = 'select Pred from P_SO where SubObj=\'' + str_SubObj + '\''
    # str_sql_cmd += ' limit 10'
    cur.execute(str_sql_cmd)
    tuple_Pred_raw = cur.fetchall()
    #
    list_Pred = tuple_res_raw_to_list(tuple_Pred_raw)
    return list_Pred

if __name__ == '__main__':

    start = time.clock()
    listSub = get_S_by_OP('11|1')
    # print time.clock() - start
    listObj = get_O_by_SP('10|1')
    # print time.clock() - start
    listPred = get_P_by_SO('10|11')
    # print time.clock() - start

    listObjPred = get_OP_by_S(10)
    # print time.clock() - start
    listSubPred = get_SP_by_O(11)
    # print time.clock() - start
    listSubObj = get_SO_by_P(1)
    # print time.clock() - start

    print listSub
    print listObj
    print listPred

    print listObjPred
    print listSubPred
    print listSubObj

    # print type(listObjPred)
    # print listObjPred[0:2]
    # print listObjPred[0][1]
