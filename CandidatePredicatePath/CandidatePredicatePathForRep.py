# generate CandidatePredicatePathForRep

# len < 5

import MySQLdb
import pdb

filePatty = open('wikipedia-instances.txt')
linesPatty = filePatty.readlines()
# fileSql = open('SQL.txt', 'w')
# dictSubjectLen1 = dict()
# listSubjectLen1 = list()
# dictSubjectLen2 = dict()
# dictObjectLen1 = dict()
# dictObjectLen2 = dict()

conn = MySQLdb.connect(host='localhost', user='root', passwd='Dbis_23508468', db='dbpedia')
cur = conn.cursor()

hashPredicateLabel = hash('<http://www.w3.org/2000/01/rdf-schema#label>')

fileRes = open('CandidatePredicatePathForRep', 'w')

for eachPattyLine in linesPatty:
    eachPattyLine = eachPattyLine.replace('\n', '')
    words = eachPattyLine.split('\t')
    if words.__len__() < 3:
        continue
    patternId = words[0]
    fileRes.write(patternId)
    patternSubject = words[1]
    patternSubject = patternSubject.replace('\"', '\\"')
    patternObject = words[2]
    patternObject = patternObject.replace('\"', '\\"')
    hashSubjectLabel = hash('\"' + patternSubject + '\"@en')
    print patternSubject + hashSubjectLabel.__str__()
    hashObjectLabel = hash('\"' + patternObject + '\"@en')
    print patternObject + hashObjectLabel.__str__()
    sqlUrlSubject = 'select Subject from S_OP WHERE ObjectPredicate=\''+hashSubjectLabel.__str__()+'s'+hashPredicateLabel.__str__()+'\''
    sqlUrlObject = 'select Subject from S_OP WHERE ObjectPredicate=\''+hashObjectLabel.__str__()+'s'+hashPredicateLabel.__str__() + '\''
    cur.execute(sqlUrlSubject)
    urlSubjectRes = cur.fetchall()
    if urlSubjectRes.__len__() == 0:
        continue
    if urlSubjectRes.__len__() == 2:
        urlSubject = urlSubjectRes[1][0]
    else:
        urlSubject = urlSubjectRes[0][0]
    cur.execute(sqlUrlObject)
    urlObjectRes = cur.fetchall()
    if urlObjectRes.__len__() == 0:
        continue
    if urlObjectRes.__len__() == 2:
        urlObject = urlObjectRes[1][0]
    else:
        urlObject = urlObjectRes[0][0]
    print urlSubjectRes
    print urlObjectRes
    print urlSubject
    print urlObject


    sqlSubjectForwardLen1 = 'select ObjectPredicate from S_OP WHERE Subject=\'' + urlSubject.__str__() + '\''
    sqlSubjectBackwardLen1 = 'select SubjectPredicate from O_SP WHERE Object=\'' + urlSubject.__str__() + '\''
    cur.execute(sqlSubjectForwardLen1)
    listSubjectTargetResLen1 = cur.fetchall()
    listSubjectTargetLen1 = list()

    # print listSubjectTargetResLen1
    for i in range(0, listSubjectTargetResLen1.__len__()):
        listSubjectTargetLen1.append(listSubjectTargetResLen1[i][0] + '[f]')
    cur.execute(sqlSubjectBackwardLen1)
    listTempRes = cur.fetchall()
    listTemp = list()
    for i in range(0, listTempRes.__len__()):
        listTemp.append(listTempRes[i][0] + '[b]')
    listSubjectTargetLen1.extend(listTemp)
    listSubjectTargetLen2 = list()
    for eachSubjectTargetLen1 in listSubjectTargetLen1:
        eachSubjectTargetLen1 = eachSubjectTargetLen1.replace('\n', '')
        TP = eachSubjectTargetLen1.split('s')
        len1Target = TP[0]
        len1Predicate = TP[1]
        sqlSubjectForwardLen2 = 'select ObjectPredicate from S_OP WHERE Subject=\'' + len1Target + '\''
        sqlSubjectBackwardLen2 = 'select SubjectPredicate from O_SP WHERE Object=\'' + len1Target + '\''
        cur.execute(sqlSubjectForwardLen2)
        listTempRes = cur.fetchall()
        listTemp = list()
        for i in range(0, listTempRes.__len__()):
            listTemp.append(listTempRes[i][0] + '[f]')
        listSubjectTargetLen2.extend(listTemp)
        cur.execute(sqlSubjectBackwardLen2)
        listTempRes = cur.fetchall()
        for i in range(0, listTempRes.__len__()):
            listTemp.append(listTempRes[i][0] + '[b]')
        listSubjectTargetLen2.extend(listTemp)
        listDelete = list()
        for i in range(0, listSubjectTargetLen2.__len__()):
            words = listSubjectTargetLen2[i].split('s')
            tempSub = words[0]
            if tempSub == hashSubjectLabel:
                listDelete.append(i)
                continue
            pdb.set_trace()
            listSubjectTargetLen2[i] = tempSub + 's' + len1Predicate + words[1]

        for i in range(listDelete.__len__() - 1, -1, -1):
            indexDelete = listDelete[i]
            del listSubjectTargetLen2[i]


    sqlObjectForwardLen1 = 'select ObjectPredicate from S_OP WHERE Subject=\'' + urlObject + '\''
    sqlObjectBackwardLen1 = 'select SubjectPredicate from O_SP WHERE Object=\'' + urlObject + '\''
    cur.execute(sqlObjectForwardLen1)
    listObjectTargetLen1 = list()
    listTempRes = cur.fetchall()
    listTemp = list()

    for i in range(0, listTempRes.__len__()):
        # you yu shi object, suoyi fangxiang yao fanzhexie
        listTemp.append(listTempRes[i][0] +'[b]' )
    listObjectTargetLen1.extend(listTemp)
    cur.execute(sqlObjectBackwardLen1)
    listTempRes = cur.fetchall()
    listTemp = list()
    for i in range(0, listTemp.__len__()):
        listTemp[i].append(listTempRes[i][0] + '[f]')
    listObjectTargetLen1.extend(listTemp)
    listObjectTargetLen2 = list()
    for eachObjectTargetLen1 in listObjectTargetLen1:
        eachObjectTargetLen1 = eachObjectTargetLen1.replace('\n', '')
        #
        TP = eachObjectTargetLen1.split('s')
        len1Target = TP[0]
        len1Predicate = TP[1]
        #
        sqlObjectForwardLen2 = 'select ObjectPredicate from S_OP WHERE Subject=\'' + len1Target + '\''
        sqlObjectBackwardLen2 = 'select SubjectPredicate from O_SP WHERE Object=\'' + len1Target + '\''
        cur.execute(sqlObjectForwardLen2)
        listTempRes = cur.fetchall()
        listTemp = list()
        for i in range(0, listTemp.__len__()):
            listTemp.append(listTempRes[i][0] + '[b]')
        listObjectTargetLen2.extend(listTemp)
        cur.execute(sqlObjectBackwardLen2)
        listTempRes = cur.fetchall()
        listTemp = list()
        for i in range(0, listTemp.__len__()):
            listTemp.append(listTempRes[i][0] + '[f]')
        listObjectTargetLen2.extend(listTemp)
        listDelete = list()
        for i in range(0, listObjectTargetLen2.__len__()):
            words = listObjectTargetLen2[i].split('s')
            tempSub = words[0]
            if tempSub == hashObjectLabel:
                listDelete.append(i)
                continue
            listObjectTargetLen2[i] += len1Predicate

        for i in range(listDelete.__len__() - 1, -1, -1):
            indexDelete = listDelete[i]
            del listObjectTargetLen2[i]

    # len = 1
    for eachTarget in listSubjectTargetLen1:
        eachTarget = eachTarget.replace('\n', '')
        words = eachTarget.split('s')
        if words[0] == hashObjectLabel:
            fileRes.write('~' + words[1])

    # len = 2
    for eachTarget in listSubjectTargetLen2:
        eachTarget = eachTarget.replace('\n', '')
        words = eachTarget.split('s')
        if words[0] == hashObjectLabel:
            fileRes.write('~' + words[1])

    # len = 3

    dictObjectLen1 = dict()
    for eachElement in listObjectTargetLen1:
        eachElement = eachElement.replace('\n', '')
        words = eachElement.split('s')
        key = words[0]
        value = words[1]
        if key not in dictObjectLen1:
            dictObjectLen1[key] = value
        else:
            dictObjectLen1[key] += '~' + value

    for eachElement in listSubjectTargetLen2:
        eachElement = eachElement.replace('\n', '')
        words = eachElement.split('s')
        key = words[0]
        value = words[1]

        if key in dictObjectLen1:
            value2 = dictObjectLen1[key]
            wordsValue = value2.split('~')
            for eachWordValue in wordsValue:
                fileRes.write('~' + value + eachWordValue)

    # len = 4

    dictObjectLen2 = dict()
    for eachElement in listObjectTargetLen2:
        eachElement = eachElement.replace('\n', '')
        words = eachElement.split('s')
        key = words[0]
        value = words[1]
        if key not in dictObjectLen2:
            dictObjectLen2[key] = value
        else:
            dictObjectLen2[key] += '~' + value

    for eachElement in listSubjectTargetLen2:
        eachElement = eachElement.replace('\n', '')
        words = eachElement.split('s')
        key = words[0]
        value = words[1]
        if key in dictObjectLen2:
            value2 = dictObjectLen2[key]
            wordsValue = value2.split('~')
            for eachWordValue in wordsValue:
                fileRes.write('~' + value + eachWordValue)

    fileRes.write('\n')
cur.close()
conn.close()
fileRes.close()
filePatty.close()












