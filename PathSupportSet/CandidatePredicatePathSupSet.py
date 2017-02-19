# coding=gbk
# CandidatePredicatePathForRep format:RelationPhraseId~Predicate[f/b]Predicate[f/b]…~Predicate[f/b]Predicate[f/b]…
# generate Predicate/Path support set and record predicate candidates at the same time
import MySQLdb
import re

conn = MySQLdb.connect(host='localhost', user='root', password='password', db='dbpedia')
cur = conn.cursor()

filePredicatePathSupSet = open('PredicatePathSupSet', 'w')
fileCandidatePredicatePathForRep = open('CandidatePredicatePathForRep')
filePredicateCandidates = open('PredicatePathCandidates', 'w')

linesCandidatePredicatePathForRep = fileCandidatePredicatePathForRep.readlines()

dictPredicatePathCandidates = dict()

for eachLine in linesCandidatePredicatePathForRep:
    eachLine = eachLine.replace('\n', '')
    words = eachLine.split('~')
    idRep = words[0]
    del words[0]  # 去掉最开始的relation phrase id
    listPath = list()
    for eachPath in words:  # 一条路径
        if eachPath in dictPredicatePathCandidates:
            dictPredicatePathCandidates[eachPath] += '~' + idRep
        else:
            dictPredicatePathCandidates[eachPath] = idRep
        wordsPath = eachPath.split(']')
        dictResEntityPair = dict()  # 保存截止当前路径的EntityPairs
        for eachPredicate in wordsPath:
            wordsPredicate = eachPredicate.split('[')  # 路径中的每一条谓语
            predicate = wordsPredicate[0]
            direction = wordsPredicate[1]
            sqlPredicateSO = 'select SO from P_SO WHERE Predicate = \'' + predicate.__str__() + '\''
            cur.execute(sqlPredicateSO)
            listSO = cur.fetchall()  # 找出所有的SO
            dictCurEntityPair = dict()  # 将找出的SO处理成dict，方便后面做连接
            for eachElement in listSO:
                wordsSO = eachElement.split('s')
                wordSubject = wordsSO[0]
                wordObject = wordsSO[1]
                if direction.__str__() == 'f':
                    dictCurEntityPair[wordSubject] = wordObject
                else:
                    dictCurEntityPair[wordObject] = wordSubject
            if dictResEntityPair.__len__() == 1:
                dictResEntityPair = dictCurEntityPair
            else:
                for eachKey in dictResEntityPair:
                    # 把当前的node，连接到下一次要做匹配连接的那个node上
                    if eachKey in dictCurEntityPair:
                        # 其实就相当于把dictResEntityPair的key换成下一个node
                        dictResEntityPair[dictCurEntityPair[eachKey]] = dictResEntityPair[eachKey]

        # 写入结果
        filePredicatePathSupSet.write(eachPath)
        for eachKey in dictResEntityPair:
            filePredicatePathSupSet.write('~')
            # 一定是先写value进去，然后再写key，因为连接方式
            filePredicatePathSupSet.write(dictResEntityPair[eachKey] + '\t' + eachKey)
        filePredicatePathSupSet.write('\n')

# 保存candidate
for eachCandidate in dictPredicatePathCandidates:
    filePredicateCandidates.write(eachCandidate + '~' + dictPredicatePathCandidates[eachCandidate] + '\n')




cur.close()
conn.close()
filePredicateCandidates.close()
filePredicatePathSupSet.close()
fileCandidatePredicatePathForRep.close()

