# -*-coding:UTF-8-*-

# 生成关系词的候选谓语路径
# 长度暂时计划不超过5
# 先从1开始，然后递增: 1,2,4……
# 结果保存在文件FileCandidatePredicatePath中，格式为：RelationPhraseId~Predicate[f/b]Predicate[f/b]…­~Predicate[f/b]Predicate[f/b]…

import MySQLdb

from GetIdByUrl import get_pred_id_by_url
from GetIdByUrl import get_ins_id_by_url

import sys
sys.path.append('..')
from MySQLConn import mysql_conn

# conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
# cur = conn.cursor()

cur = mysql_conn

if __name__ == '__main__':
    fileWikiIns = open('../patty-dataset-freebase/wikipedia-instances.txt')
    linesWikiIns = fileWikiIns.readlines()

    strUrlLabel = 'http://www.w3.org/2000/01/rdf-schema#label'
    intPredLabelId = get_pred_id_by_url(strUrlLabel)

    fileRes = open('FileCandidatePredicatePath', 'w')

    for eachWikiIns in linesWikiIns:
        eachWikiIns = eachWikiIns.replace('\n', '')
        words = eachWikiIns.split('\t')
        if words.__len__() < 3:
            continue
        strRepId = words[0]
        fileRes.write(strRepId)
        strRepSub = words[1]
        strRepSub = strRepSub.replace('\"', '\\"')
        strRepObj = words[2]
        strRepObj = strRepObj.replace('\"', '\\"')
        intRepSubId = get_ins_id_by_url('\"' + strRepSub + '\"@en')
        intRepObjId = get_obj_id_by_url('\"' + strRepObj + '\"@en')





