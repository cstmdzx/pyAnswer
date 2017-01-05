import MySQLdb
import os
import time

def split_prefix(str_object):
        words = testLine.split('/')

        intWordsLen = words.__len__()
        strInstance = words[intWordsLen - 1]

        strPrefix = ''
        for intIndex in range(0, intWordsLen - 1):
            strPrefix += words[intIndex]
        if strPrefix in dictPrefix:



fileS_OP = open('S_OP','w')
fileOP_S = open('OP_S','w')
fileSO_P = open('SO_P','w')
fileP_SO = open('P_SO','w')
fileSP_O = open('SP_O','w')
fileO_SP = open('O_SP','w')

pathDBpedia = '/home/nklyp/pyAnswer/dbpediattl'
fileNames = os.listdir(pathDBpedia)

print time.time()

dictPrefix = dict()
intPrefixCount = 0

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
            continue
        testLine = linesData[0]

        strSubject = listSPO[0]
        strPredicate = listSPO[1]
        strObject = listSPO[2]
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
        print hashSubject
        print hashObject
        print hashPredicate
        print hashOP
        '''
        fileS_OP.write(hashSubject.__str__() + '\t' + hashOP + '\n')
        fileP_SO.write(hashPredicate.__str__() + '\t' + hashSO + '\n')
        fileO_SP.write(hashObject.__str__() + '\t' + hashSP + '\n')
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

