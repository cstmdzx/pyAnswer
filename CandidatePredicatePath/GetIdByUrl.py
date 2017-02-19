# -*-coding:UTF-8-*-

import MySQLdb
import pdb
import time # 测试时间

import sys
sys.path.append('..')
from MySQLConn import mysql_conn

# conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
# cur = conn.cursor()
cur = mysql_conn()

# 从PredicateId中根据Pred获得Id
def get_pred_id_by_url(url):
    str_sql_cmd = 'select Id from PredicateId WHERE Pred = \'' + url.__str__() + '\''
    cur.execute(str_sql_cmd)
    tuple_pred_id = cur.fetchall()

    #-1 表示没有，-2表示不止一个，不然就返回第一个，每个是个tuple，因此选tuple的第一个
    if tuple_pred_id.__len__() == 0:
        return -1
    elif tuple_pred_id.__len__() > 1:
        return -2
    elif tuple_pred_id.__len__() == 1:
        return tuple_pred_id[0][0]
    else:
        print 'unexcepted error in get_pred_id_by_url'

# 从InstanceId中根据Ins获得Id
def get_ins_id_by_url(url):
    # ins的不一定是url，也可能是纯文本
    str_sql_cmd = 'select Id from InstanceId WHERE Ins = \'' + url.__str__() + '\''
    # print str_sql_cmd
    cur.execute(str_sql_cmd)
    tuple_ins_id = cur.fetchall()

    #-1 表示没有，-2表示不止一个，不然就返回第一个，每个是个tuple，因此选tuple的第一个
    if tuple_ins_id.__len__() == 0:
        return -1
    elif tuple_ins_id.__len__() > 1:
        return -2
    elif tuple_ins_id.__len__() == 1:
        return tuple_ins_id[0][0]
    else:
        print 'unexcepted error in get_ins_id_by_url'

# 测试部分
if __name__ == '__main__':
    strPredUrl = 'http://dbpedia.org/property/leagueTopScorer'
    start = time.clock()
    intPredId = get_pred_id_by_url(strPredUrl)
    end = time.clock()
    print end - start # 输出运行时间
    print intPredId
    print type(intPredId) # 显示类型

    strInsUrl = '"Strafgesetzbuch"@en'
    start = time.clock()
    intInsId = get_ins_id_by_url(strInsUrl)
    end = time.clock()
    print end - start # 输出运行时间
    print intInsId
    print type(intInsId) # 显示类型

