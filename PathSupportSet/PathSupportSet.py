# -*-coding:UTF-8-*-

# 生成每个Path的支持集，集合中的每个元素为一个词对，这个集和可以被表示为一个向量

# CandidatePredicatePathForRep format:RelationPhraseId~Predicate[f/b]Predicate[f/b]...~Predicate[f/b]Predicate[f/b]...­

import MySQLdb
import re
import sys
import time

from GetEntityPairByPath import get_entity_pair_by_path

'''
import sys
sys.path.append('..')
from MySQLConn import mysql_conn
cur = mysql_conn()
'''

if __name__ == '__main__':
    strFilePathRes = './PathRes/'
    strFileAssociateRes = './AssociateRes/'

    start = time.time()
    filePredPathSupSet = open(strFilePathRes + 'FilePredPathSupSetLen2100<<150', 'w') # 保存结果词对
    filePredPath = open('../SpeedUp/FilePredicatePath/Len2100<<150', 'r') # 读取之前的结果, 这里保存的之前的候选路径
    filePredPathAssociateRep = open(strFileAssociateRes + 'FilePredPathAssociateRepLen2100<<150', 'w') #

    linesPredPath = filePredPath.readlines()
    dictPredPathAssociateRep = dict()

    print 'File Read Finish, Time: %f' % (time.time() - start)
    intFlag = 0
    intExist = 0
    for eachRepIdPredPath in linesPredPath:
        intFlag += 1
        if intFlag % 1000 == 0:
            # print intExist
            # intExist = 0
            print intFlag
            print time.time() - start
        eachRepIdPredPath = eachRepIdPredPath.replace('\n', '')
        words = eachRepIdPredPath.split('~')
        strRepId = words[0]
        del words[0] # 去掉RepId,剩下的全是path

        for eachPath in words:
            if eachPath in dictPredPathAssociateRep:
                dictPredPathAssociateRep[eachPath] += '~' + strRepId
                # intExist += 1
                continue # 查出过匹配词对的不再继续去匹配，结果应该也写在硬盘上了
            else:
                dictPredPathAssociateRep[eachPath] = strRepId

            try:
                listEntityPair = get_entity_pair_by_path(eachPath)
            except Exception as e:
                print e
                print eachPath
                continue
            except KeyboardInterrupt:
                sys.exit(0)
            filePredPathSupSet.write(eachPath)
            for eachEntityPair in listEntityPair:
                filePredPathSupSet.write(('~' + eachEntityPair['sl'] + '\t' + eachEntityPair['ol']).encode('UTF-8'))
            filePredPathSupSet.write('\n')

    # 把与每个PredPath有关的RepId保存下来，后面计算相似度
    for eachPredPathAssociateRep in dictPredPathAssociateRep:
        filePredPathAssociateRep.write(eachPredPathAssociateRep + '~' + dictPredPathAssociateRep[eachPredPathAssociateRep] + '\n')

    filePredPathSupSet.close()
    filePredPath.close()
    filePredPathAssociateRep.close()

