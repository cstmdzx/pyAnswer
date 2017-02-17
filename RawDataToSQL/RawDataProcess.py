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
def split_prefix(str_rdf):  # enum the prefix
    # failed
    global intPrefixCount
    # print intPrefixCount
    words = str_rdf.split('/')
    intWordsLen = words.__len__()
    strInstance = words[intWordsLen - 1]
    strPrefix = ''
    for intIndex in range(0, intWordsLen - 1):
        strPrefix += words[intIndex] + '/'
    if strPrefix in dictPrefix:
        strRes = dictPrefix[strPrefix]
    else:
        strRes = 'p' + str(intPrefixCount) + '/'
        dictPrefix[strPrefix] = strRes
        intPrefixCount += 1
    return strRes + strInstance

strPath = './res/'
fileS_OP = open(strPath + 'S_OP','w')
fileOP_S = open(strPath + 'OP_S','w')
fileSO_P = open(strPath + 'SO_P','w')
fileP_SO = open(strPath + 'P_SO','w')
fileSP_O = open(strPath + 'SP_O','w')
fileO_SP = open(strPath + 'O_SP','w')

pathDBpedia = '/home/nklyp/pyAnswer/dbpediattl'
fileNames = os.listdir(pathDBpedia)

print time.time()


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
        strOPId = strObjectId + '|' + strPredicateId
        strSOId = strSubjectId + '|' + strObjectId
        strSPId = strSubjectId + '|' + strPredicateId
        fileS_OP.write(strSubjectId + '\t' + strOPId + '\n')
        fileP_SO.write(strPredicateId + '\t' + strSOId + '\n')
        fileO_SP.write(strObjectId + '\t' + strSPId + '\n')
        '''
        intListSPOLen = listSPO.__len__() - 1
        # print listSPO[intListSPOLen]
        for i in range(3, intListSPOLen):
            strObject += ' ' + listSPO[i]
        # print strObject
        hashSubject = hash(strSubject)
        hashPredicate = hash(strPredicate)
        hashObject = hash(strObject)
        hashOP = hashObject.__str__() + 's' + hashPredicate.__str__()
        hashSO = hashSubject.__str__() + 's' + hashObject.__str__()
        hashSP = hashSubject.__str__() + 's' + hashPredicate.__str__()
        '''


        '''
        print hashSubject
        print hashObject
        print hashPredicate
        print hashOP
        '''

        '''
        fileS_OP.write(hashSubject.__str__() + '\t' + hashOP + '\n')
        fileP_SO.write(hashPredicate.__str__() + '\t' + hashSO + '\n')
        fileO_SP.write(hashObject.__str__() + '\t' + hashSP + '\n')
        '''


#        fileSP_O.write(hashSP + '\t' + hashObject)
#        fileSO_P.write(hashSO + '\t' + hashPredicate)
#        fileOP_S.write(hashOP + '\t' + hashSubject)
        '''
        insertFunction(cur, 'S_OP', 'is', hashSubject, hashOP)
        insertFunction(cur, 'P_SO', 'is', hashPredicate, hashSO)
        insertFunction(cur, 'O_SP', 'is', hashObject, hashSP)
        insertFunction(cur, 'SP_O', 'si', hashSP, hashObject)
        insertFunction(cur, 'SO_P', 'si', hashSO, hashPredicate)
        insertFunction(cur, 'OP_S', 'si', hashOP, hashSubject)
        '''
    print eachFileName + 'finish'

# connect.commit()

fileS_OP.close()
fileP_SO.close()
fileO_SP.close()
fileSP_O.close()
fileSO_P.close()
fileOP_S.close()

# cur.close()
# connect.close()


fileInstanceId = open('InstanceId', 'w')
filePredicateId = open('PredicateId', 'w')
for eachInstance in dictInstance:
    fileInstanceId.write(eachInstance + '\t' + str(dictInstance[eachInstance]) + '\n')
for eachPredicate in dictPredicate:
    filePredicateId.write(eachPredicate + '\t' + str(dictPredicate[eachPredicate]) + '\n')

fileInstanceId.close()
filePredicateId.close()

