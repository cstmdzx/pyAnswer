# -*-coding:UTF-8-*-

# 直接生成SPO的三元祖，考虑构建多列索引

import MySQLdb
import os
import time

dictPrefix = dict()
dictInstance = dict()
dictPredicate = dict()
intInstanceCount = 0
intPredicateCount = 0

global intPrefixCount
intPrefixCount = 0

strPath = './resSPO/'

fileSPO = open(strPath + 'SPO', 'w')

pathDBpedia = '/home/nklyp/pyAnswer/dbpediattl'
fileNames = os.listdir(pathDBpedia)

start = time.clock()
print start


for eachFileName in fileNames:
    fileData = open(pathDBpedia + '/' + eachFileName)
    # fileData = open(eachFileName)
    linesData = fileData.readlines()
    print eachFileName
    count = 0


    for eachData in linesData:
        count = count + 1
        '''
        if count % 10000 == 0:
            print count
            print time.time()
            connect.commit()
        '''
        eachData = eachData.replace('\n', '')
        eachData = eachData.replace('<', '')
        eachData = eachData.replace('>', '')

        listSPO = eachData.split(' ')
        if listSPO.__len__() < 3:
            print 'shao'
            continue

        strSubject = listSPO[0]
        if strSubject in dictInstance:
            intSubjectId = dictInstance[strSubject]
        else:
            dictInstance[strSubject] = intInstanceCount
            intSubjectId = intInstanceCount
            intInstanceCount += 1

        strPredicate = listSPO[1]
        if strPredicate in dictPredicate:
            intPredicate = dictPredicate[strPredicate]
        else:
            dictPredicate[strPredicate] = intPredicateCount
            intPredicateId = intPredicateCount
            intPredicateCount += 1

        del listSPO[0]
        del listSPO[0]

        strObject = listSPO[0]
        del listSPO[0]
        intLen = listSPO.__len__()
        # print intLen
        # print listSPO

        if intLen > 0:
            if listSPO[intLen - 1] == '.':
                del listSPO[intLen - 1] # 注意，结尾有可能是个‘.’，删了他
            for eachWord in listSPO:
                strObject += ' ' + eachWord
        # print strObject

        if strObject in dictInstance:
            intObjectId = dictInstance[strObject]
        else:
            dictInstance[strObject] = intInstanceCount
            intObjectId = intInstanceCount
            intInstanceCount += 1

        strSubjectId = str(intSubjectId)
        strPredicateId = str(intPredicateId)
        strObjectId = str(intObjectId)

        fileSPO.write(strSubjectId + '\t' + strPredicateId + '\t' + strObjectId + '\n')

    print eachFileName + 'finish'
'''
fileS_OP.close()
fileP_SO.close()
fileO_SP.close()
fileSP_O.close()
fileSO_P.close()
fileOP_S.close()
'''

fileInstanceId = open(strPath + 'InstanceId', 'w')
filePredicateId = open(strPath + 'PredicateId', 'w')
for eachInstance in dictInstance:
    fileInstanceId.write(eachInstance + '\t' + str(dictInstance[eachInstance]) + '\n')
for eachPredicate in dictPredicate:
    filePredicateId.write(eachPredicate + '\t' + str(dictPredicate[eachPredicate]) + '\n')

end = time.clock()
print end
print end - start


fileInstanceId.close()
filePredicateId.close()

