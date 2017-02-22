# generate CandidatePredicatePathForRep
# CandidatePredicatePathForRep format:RelationPhraseId~Predicate[f/b]Predicate[f/b]…~Predicate[f/b]Predicate[f/b]…
# len < 5

import MySQLdb

filePatty = open('wikipedia-instances.txt')
linesPatty = filePatty.readlines()
# fileSql = open('SQL.txt', 'w')
# dictSubjectLen1 = dict()
# listSubjectLen1 = list()
# dictSubjectLen2 = dict()
# dictObjectLen1 = dict()
# dictObjectLen2 = dict()

conn = MySQLdb.connect(host='localhost', user='root', password='password', db='dbpedia')
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
    hashObjectLabel = hash('\"' + patternObject + '\"@en')
    sqlUrlSubject = 'select S from OP_S WHERE OP=\''+hashSubjectLabel.__str__()+'s'+hashPredicateLabel.__str__()+'\''
    sqlUrlObject = 'select S from OP_S WHERE OP=\''+hashObjectLabel.__str__()+'s'+hashPredicateLabel.__str__() + '\''
    urlSubject = cur.execute(sqlUrlSubject)[0]
    urlObject = cur.execute(sqlUrlObject)[0]

    # 处理Subject，筛出两层路径
    sqlSubjectForwardLen1 = 'select OP from S_OP WHERE S=\'' + urlSubject + '\''
    sqlSubjectBackwardLen1 = 'select SP from O_SP WHERE O=\'' + urlSubject + '\''
    cur.execute(sqlSubjectForwardLen1)
    listSubjectTargetLen1 = cur.fetchall()  # 第一层
    for i in range(0, listSubjectTargetLen1.__len__()):
        listSubjectTargetLen1[i] += '[f]'
    cur.execute(sqlSubjectBackwardLen1)
    listTemp = cur.fetchall()
    for i in range(0, listTemp.__len__()):
        listTemp[i] += '[b]'
    listSubjectTargetLen1.extend(listTemp)
    listSubjectTargetLen2 = list()  # 第二层
    for eachSubjectTargetLen1 in listSubjectTargetLen1:
        eachSubjectTargetLen1 = eachSubjectTargetLen1.replace('\n', '')
        TP = eachSubjectTargetLen1.split('s')
        len1Target = TP[0]
        len1Predicate = TP[1]
        sqlSubjectForwardLen2 = 'select OP from S_OP WHERE S=\'' + len1Target + '\''
        sqlSubjectBackwardLen2 = 'select SP from O_SP WHERE O=\'' + len1Target + '\''
        cur.execute(sqlSubjectForwardLen2)
        listTemp = cur.fetchall()
        for i in range(0, listTemp.__len__()):
            listTemp[i] += '[f]'
        listSubjectTargetLen2.extend(listTemp)
        cur.execute(sqlSubjectBackwardLen2)
        listTemp = cur.fetchall()
        for i in range(0, listTemp.__len__()):
            listTemp[i] += '[b]'
        listSubjectTargetLen2.extend(listTemp)
        listDelete = list()
        for i in range(0, listSubjectTargetLen2.__len__()):
            words = listSubjectTargetLen2[i].split('s')
            tempSub = words[0]
            if tempSub == hashSubjectLabel:
                listDelete.append(i)
                continue
            listSubjectTargetLen2[i] += len1Predicate
        # 删除开始那个节点，不删会出现重复重复路径，
        for i in range(listDelete.__len__() - 1, -1, -1):
            indexDelete = listDelete[i]
            del listSubjectTargetLen2[i]

    # 处理Object
    sqlObjectForwardLen1 = 'select OP from S_OP WHERE S=\'' + urlObject + '\''
    sqlObjectBackwardLen1 = 'select SP from O_SP WHERE O=\'' + urlObject + '\''
    cur.execute(sqlObjectForwardLen1)
    listObjectTargetLen1 = cur.fetchall()  # 第一层
    for i in range(0, listObjectTargetLen1.__len__()):
        listSubjectTargetLen1[i] += '[f]'
    cur.execute(sqlObjectBackwardLen1)
    listTemp = cur.fetchall()
    for i in range(0, listTemp.__len__()):
        listTemp[i] += '[b]'
    listObjectTargetLen1.extend(listTemp)
    listObjectTargetLen2 = list()  # 第二层
    for eachObjectTargetLen1 in listObjectTargetLen1:
        eachObjectTargetLen1 = eachObjectTargetLen1.replace('\n', '')
        #
        TP = eachObjectTargetLen1.split('s')
        len1Target = TP[0]
        len1Predicate = TP[1]
        #
        sqlObjectForwardLen2 = 'select OP from S_OP WHERE S=\'' + len1Target + '\''
        sqlObjectBackwardLen2 = 'select SP from O_SP WHERE O=\'' + len1Target + '\''
        cur.execute(sqlObjectForwardLen2)
        listTemp = cur.fetchall()
        for i in range(0, listTemp.__len__()):
            listTemp[i] += '[f]'
        listObjectTargetLen2.extend(listTemp)
        cur.execute(sqlObjectBackwardLen2)
        listTemp = cur.fetchall()
        for i in range(0, listTemp.__len__()):
            listTemp[i] += '[b]'
        listObjectTargetLen2.extend(listTemp)
        listDelete = list()
        for i in range(0, listObjectTargetLen2.__len__()):
            words = listObjectTargetLen2[i].split('s')
            tempSub = words[0]
            if tempSub == hashObjectLabel:
                listDelete.append(i)
                continue
            listObjectTargetLen2[i] += len1Predicate
        # 删除开始那个节点，不删会出现重复重复路径，
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
    # 建个词典
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

    for eachElement in listSubjectTargetLen1:
        eachElement = eachElement.replace('\n', '')
        words = eachElement.split('s')
        key = words[0]
        value = words[1]

        if key in dictObjectLen1:
            value2 = dictObjectLen1[key]
            wordsValue = value2.split('~')
            for eachWordValue in wordsValue:
                fileRes.write('~' + value + dictObjectLen1[key])

    # len = 4
    # 建个词典
    dictObjectLen2 = dict()  # listObjectTargetLen2的每个元素，O做key，path做value，
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
                fileRes.write('~' + value + dictObjectLen2[key])

    fileRes.write('\n')
cur.close()
conn.close()
fileRes.close()
filePatty.close()












