# -*-coding:UTF-8-*-

# 生成关系词的候选谓语路径
# 长度暂时计划不超过5
# 先从1开始，然后递增: 1,2,4……
# 结果保存在文件FileCandidatePredicatePath中，格式为：RelationPhraseId~Predicate[f/b]Predicate[f/b]…­~Predicate[f/b]Predicate[f/b]…

# 如果分开跑，Len2和Len3的地方得修改一下，整体一起跑就没事，dictObjLen1现在是在Len2上建的

import MySQLdb

from GetIdByUrl import get_pred_id_by_url
from GetIdByUrl import get_ins_id_by_url

import sys
sys.path.append('..')
from MySQLConn import mysql_conn

from GetValueByIndex import get_S_by_OP
from GetValueByIndex import get_O_by_SP
from GetValueByIndex import get_P_by_SO
from GetValueByIndex import get_SP_by_O
from GetValueByIndex import get_SO_by_P
from GetValueByIndex import get_OP_by_S

# conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpd_useid')
# cur = conn.cursor()

cur = mysql_conn

if __name__ == '__main__':
    fileWikiIns = open('../patty-dataset-freebase/wikipedia-instances.txt')
    linesWikiIns = fileWikiIns.readlines()

    strUrlLabel = 'http://www.w3.org/2000/01/rdf-schema#label'
    intPredLabelId = get_pred_id_by_url(strUrlLabel)

    fileRes = open('FileCandidatePredicatePath', 'w')
    filePredPathLen1 = open(strResPath + 'Len1', 'w')
    filePredPathLen2 = open(strResPath + 'Len2', 'w')
    filePredPathLen3 = open(strResPath + 'Len3', 'w')
    filePredPathLen4 = open(strResPaht + 'Len4', 'w')

    for eachWikiIns in linesWikiIns:
        eachWikiIns = eachWikiIns.replace('\n', '')
        words = eachWikiIns.split('\t')
        if words.__len__() < 3:
            continue

        strRepId = words[0]
        # fileRes.write(strRepId)
        filePredPathLen1.write(strRepId)
        filePredPathLen2.write(strRepId)
        filePredPathLen3.write(strRepId)
        filePredPathLen4.write(strRepId)

        strRepSub = words[1]
        strRepSub = strRepSub.replace('\"', '\\"')
        strRepObj = words[2]
        strRepObj = strRepObj.replace('\"', '\\"')
        intRepSubId = get_ins_id_by_url('\"' + strRepSub + '\"@en')
        intRepObjId = get_obj_id_by_url('\"' + strRepObj + '\"@en')

        # 处理subject，筛出两层路径
        # 周围第一圈，步长为1的所有谓语和ins
        listSubTargetLen1 = get_OP_by_S(intRepSubId) # forward
        for i in range(0, listSubTargetLen1.__len__()):
            listSubTargetLen1[i] += '[f]'
        listTemp = get_SP_by_O(intRepSubId) # backward
        for i in range(0, listTemp.__len__()):
            listTemp[i] += '[b]'
        listSubTargetLen1.extend(listTemp)

        # 周围第二圈
        listSubTargetLen2 = list()
        for eachSubTarget in listSubTargetLen1:
            # eachSubTargetLen1 = eachSubTargetLen1.replace('\n', '') # ke neng meiyong
            words = eachSubTargetLen1.split('|') # 分开，取ins，这里的谓语是带着方向[f/b]的
            strIns = words[0]
            strPred = words[1]
            listTemp = get_OP_by_S(int(strIns)) # forward
            for i in range(0, listTemp.__len__()):
                listTemp[i] += '[f]'
            listSubTargetLen2.extend(listTemp)
            listTemp = get_SP_by_O(int(strIns)) # backward
            for i in range(0, listTemp.__len__()):
                listTemp[i] += '[b]'
            listSubTargetLen2.extend(listTemp)

            # 删去第二圈里的回到出发点的ins,
            # 要不就出现一个环，错误的东西会越来越多
            listDelete = list() # 用来保存所有应该被删除的点的id
            for i in range(0, listSubTargetLen2.__len__()):
                words = listSubTargetLen2[i].split('|')
                strTempSub = words[0]
                if strTempSub == str(intRepSubId):
                    listDelete.append(i)
                    continue
                listSubTargetLen2[i] += strPred
                # len2里也是ins|pred[f/b]pred[f/b]

            for i in range(listDelete.__len__()-1, -1, -1):
                intIndexDelete = listDelete[i]
                del listSubjectTargetLen2[i]

        # 处理object，同样的思路,
        # 但是f和b要换以下，因为这次是从target出发的
        listObjTargetLen1 = get_OP_by_S(intRepObjId) # forward
        for i in range(0, listObjTargetLen1.__len__()):
            listObjTargetLen1[i] += '[b]'
        listTemp = get_SP_by_O(intRepObjId) # backward
        for i in range(0,listTemp.__len__()):
            listTemp[i] += '[f]'
        listObjTargetLen1.extend(listTemp)
        listObjTargetLen2 = list()
        # 周围第二圈
        for eachObjTargetLen1 in listObjTargetLen1:
            # eachObjTargetLen1 = eachObjTargetLen1.replace('\n', '')
            words = eachObjTargetLen1.split('|')# 分开，取ins，这里的谓语是带着方向[f/b]的
            strIns = words[0]
            strPred = words[1]
            listTemp = get_OP_by_S(int(strIns)) # forward
            for i in range(0, listTemp.__len__()):
                listTemp[i] += '[b]'
            listObjTargetLen2.extend(listTemp)
            listTemp = get_SP_by_O(int(strIns)) # backward
            for i in range(0, listTemp.__len__()):
                listTemp[i] += '[f]'
            listObjTargetLen2.extend(listTemp)

            # 删去第二圈里的回到出发点的ins,
            # 要不就出现一个环，错误的东西会越来越多
            listDelete = list()
            for i in range(0, listObjTargetLen2.__len__()):
                words = listObjTargetLen2[i].split('|')
                strTempSub = words[0]
                if strTempSub = str(intRepObjId):
                    listDelete.append(i)
                    continue
                listObjTargetLen2[i] += strPred

            for i in range(listDelete.__len__()-1, -1, -1):
                intIndexDelete = listDelete[i]
                del listObjTargetLen2[i]

        # 一会回来改一下，分成四个文件来分别求
        strResPath = './FilePredicatePath/'
        # len 1
        for eachTarget in listSubTargetLen1:
            words = eachTarget.split('|')
            if words[0] == str(intRepObjId):
                filePredPathLen1.write('~' + words[1])
        filePredPathLen1.write('\n')

        # len 2 , zhu yao jiushi zhege
        '''
        for eachTarget in listSubTargetLen2:
            words = eachTarget.split('|')
            if words[0] == str(intRepObjId):
                filePredPathLen2.write('~' + words[1])
        filePredPathLen2.write('\n')
        '''
        dictObjLen1 = dict()
        for eachTarget in listObjTargetLen1:
            words = eachTarget.split('|')
            strObj = words[0]
            strPred = words[1]
            if strObj not in dictObjLen1:
                dictObjLen1[strObj] = strPred
            else:
                dictObjLen1[strObj] += '~' + strPred

        for eachTarget in listSubTargetLen1:
            words = eachTarget.split('|')
            strSub = words[0]
            strPred = words[1]

            if strSub in dictObjLen1:
                words2 = dictObjLen1[strSub].split('~')
                for eachPredPath in words2:
                    filePredPathLen2.write('~' + strPred + eachPredPath)
        filePredPathLen2.write('\n')

        # len 3
        '''
        dictObjLen1 = dict()
        for eachTarget in listObjTargetLen1:
            words = eachTarget.split('|')
            strObj = words[0]
            strPred = words[1]
            if strObj not in dictObjLen1:
                dictObjLen1[strObj] = strPred
            else:
                dictObjLen1[strObj] += '~' + strPred
        '''

        for eachTarget in listSubTargetLen2:
            words = eachTarget.split('|')
            strSub = words[0]
            strPred = words[1]

            if strSub in dictObjLen1:
                words2 = dictObjLen1[strSub].split('~')
                for eachPredPath in words2:
                    filePredPathLen3.write('~' + strPred + eachPredPath)
        filePredPathLen3.write('\n')

        # len 4
        dictObjLen2 = dict()
        for eachTarget in listObjTargetLen2:
            words = eachTarget.split('|')
            strObj = words[0]
            strPred = words[1]
            if strObj not in dictObjLen2:
                dictObjLen2[strObj] = strPred
            else:
                dictObjLen2[strObj] += '~' + strPred

        for eachTarget in listSubTargetLen2:
            words = eachTarget.split('|')
            strSub = words[0]
            strPred = words[1]
            if strSub in dictObjLen2:
                words2 = dictObjLen2[strSub].split('~')
                for eachPredPath in words2:
                    filePredPathLen4.write('~' + strPred + eachPredPath)
        filePredPathLen4.write('\n')
        # fileRes.write('\n')

    cur.close()
    fileRes.close()
    filePredPathLen1.close()
    filePredPathLen2.close()
    filePredPathLen3.close()
    filePredPathLen4.close()
    fileWikiIns.close()

