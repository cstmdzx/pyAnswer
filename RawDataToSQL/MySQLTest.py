'''
alter table S_OP modify column ObjectPredicate varchar(45);
alter table OP_S modify column ObjectPredicate varchar(45);
alter table P_SO modify column SubjectObject varchar(45);
alter table SO_P modify column SubjectObject varchar(45);
alter table O_SP modify column SubjectPredicate varchar(45);
alter table SP_O modify column SubjectPredicate varchar(45);

alter table S_OP modify column Subject bigint;
alter table OP_S modify column Subject bigint;
alter table P_SO modify column Predicate bigint;
alter table SO_P modify column Predicate bigint;
alter table O_SP modify column Object bigint;
alter table SP_O modify column Object bigint;

'''

import MySQLdb
import os
import time

fileS_OP = open('S_OP','w')
fileOP_S = open('OP_S','w')
fileSO_P = open('SO_P','w')
fileP_SO = open('P_SO','w')
fileSP_O = open('SP_O','w')
fileO_SP = open('O_SP','w')
'''
def insertFunction(cursor, table, pattern, v1, v2):
    if pattern == 'si':
        cursor.execute('insert into %s values(\'%s\', %d)'%(table, v1.__str__(), v2))
    if pattern == 'is':
        cursor.execute('insert into %s values(%d, \'%s\')'%(table, v1, v2.__str__()))
'''
pathDBpedia = '/home/linuxhg/dbpediattl'
fileNames = os.listdir(pathDBpedia)
# fileNames = {'labeltest.ttl'}

# connect = MySQLdb.connect(host='localhost', user='root', passwd='password', db='dbpedia', port=3306)
# cur = connect.cursor()

print time.time()

for eachFileName in fileNames:
    fileData = open(pathDBpedia + '/' + eachFileName)
    # fileData = open(eachFileName)
    linesData = fileData.readlines()
    print eachFileName
    count = 0
    '''
    if count % 100000 == 0:
         cur.commit()
    '''
    for eachData in linesData:
        count = count + 1
        '''
        if count % 10000 == 0:
            print count
            print time.time()
            connect.commit()
        '''
        eachData = eachData.replace('\n', '')
        listSPO = eachData.split(' ')
        if listSPO.__len__() < 3:
            continue
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

