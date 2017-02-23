# -*-coding:UTF-8-*-

# 生成每个Path的支持集，集合中的每个元素为一个词对，这个集和可以被表示为一个向量

# CandidatePredicatePathForRep format:RelationPhraseId~Predicate[f/b]Predicate[f/b]...~Predicate[f/b]Predicate[f/b]...­

import MySQLdb
import re

from GetEntityPairByPath import get_entity_pair_by_path

'''
import sys
sys.path.append('..')
from MySQLConn import mysql_conn
cur = mysql_conn()
'''

if __name__ == '__main__':
    filePredPathSupSet = open('FilePredPathSupSet', 'w') # 保存结果词对
    filePredPath = open('FilePredicatePath', 'r') # 读取之前的结果, 这里保存的之前的候选路径
    filePredPathAssociateRep = open('FilePredPathAssociateRep', 'w') #

    linesPredPath = filePredPath.readlines()
    dictPredPathAssociateRep = dict()

    for eachRepIdPredPath in linesPredPath:
        eachRepIdPredPath = eachRepIdPredPath.replace('\n', '')
        words = eachRepIdPredPath.split('~')
        strRepId = words[0]
        del words[0] # 去掉RepId,剩下的全是path

        for eachPath in words:
            filePredPathSupSet.write(eachPath)
            if eachPath in dictPredPathAssociateRep:
                dictPredPathAssociateRep[eachPath] += '~' + strRepId
                continue # 查出过匹配词对的不再继续去匹配，结果应该也写在硬盘上了
            else:
                dictPredPathAssociateRep[eachPath] = strRepId

            listEntityPair = get_entity_pair_by_path(eachPath)
            for eachEntityPair in listEntityPair:
                filePredPathSupSet.write('~' + eachEntityPair[0] + '\t' + eachEntityPair[1])
            filePredPathSupSet.write('\n')

    # 把与每个PredPath有关的RepId保存下来，后面计算相似度
    for eachPredPathAssociateRep in dictPredPathAssociateRep:
        filePredPathAssociateRep.write(eachPredPathAssociateRep + '~' + dictPredPathAssociateRep[eachPredPathAssociateRep] + '\n')

    filePredPathSupSet.close()
    filePredPath.close()
    filePredPathAssociateRep.close()

