# -*-coding:UTF-8-*-

# 连接mysql

import MySQLdb

def mysql_conn():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
    cur = conn.cursor()
    return cur

if __name__ == '__main__':
    curr = mysql_conn()
    strSqlCmd = 'select * from S_OP limit 10'
    curr.execute(strSqlCmd)
    listRes = curr.fetchall()
    print listRes

