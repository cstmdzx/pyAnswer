# -*-coding:UTF-8-*-

# 用来从数据库中根据索引值选出对应值
# 主要包括根据S选OP，根据O选SP，根据P选SO
# 以及反过来

import MySQLdb

from ../MySQLConn import mysql_conn

# conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
# cur = conn.cursor()
cur = mysql_conn()

def get_OP_by_S(int_Sub):
    str_sql_cmd = 'select ObjPred from S_OP where Sub=' + str(int_Sub)
    cur.execute(str_sql_cmd)
    list_ObjPred_raw = cur.fetchall()
    # 由于每一个都是tuple，因此返回所有tuple的第一个
    return list_ObjPred_raw[:][0]

def get_SP_by_O(int_Obj):
    str_sql_cmd = 'select SubPred from O_SP where Obj=' + str(int_Obj)
    cur.execute(str_sql_cmd)
    list_SubPred_raw = cur.fetchall()
    #
    return list_SubPred_raw[:][0]

def get_SO_by_P(int_Pred):
    str_sql_cmd = 'select SubObj from P_SO where Pred=' + str(int_Pred)
    cur.execute(str_sql_cmd)
    list_SubObj_raw = cur.fetchall()
    #
    return list_SubObj_raw[:][0]

def get_S_by_OP(str_ObjPred):
    str_sql_cmd = 'select Sub from S_OP where ObjPred=\'' + str_ObjPred + '\''
    cur.execute(str_sql_cmd)
    list_Sub_raw = cur.fetchall()
    #
    return list_Sub_raw[:][0]

def get_O_by_SP(str_SubPred):
    str_sql_cmd = 'select Obj from O_SP where SubPred=\'' + str_SubPred + '\''
    cur.execute(str_sql_cmd)
    list_Obj_raw = cur.fetchall()
    #
    return list_Obj_raw[:][0]

def get_P_by_SO(str_SubObj):
    str_sql_cmd = 'select Pred from P_SO where SubObj=\'' + str_SubObj + '\''
    cur.execute(str_sql_cmd)
    list_Pred_raw = cur.fetchall()
    #
    return list_Pred_raw[:][0]

if __name__ == '__main__':
    listSub = get_Sub_by_Obj






