# coding=gbk
# CandidatePredicatePathForRep format:RelationPhraseId~Predicate[f/b]Predicate[f/b]��~Predicate[f/b]Predicate[f/b]��
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
    del words[0]  # ȥ���ʼ��relation phrase id
    listPath = list()
    for eachPath in words:  # һ��·��
        if eachPath in dictPredicatePathCandidates:
            dictPredicatePathCandidates[eachPath] += '~' + idRep
        else:
            dictPredicatePathCandidates[eachPath] = idRep
        wordsPath = eachPath.split(']')
        dictResEntityPair = dict()  # �����ֹ��ǰ·����EntityPairs
        for eachPredicate in wordsPath:
            wordsPredicate = eachPredicate.split('[')  # ·���е�ÿһ��ν��
            predicate = wordsPredicate[0]
            direction = wordsPredicate[1]
            sqlPredicateSO = 'select SO from P_SO WHERE Predicate = \'' + predicate.__str__() + '\''
            cur.execute(sqlPredicateSO)
            listSO = cur.fetchall()  # �ҳ����е�SO
            dictCurEntityPair = dict()  # ���ҳ���SO�����dict���������������
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
                    # �ѵ�ǰ��node�����ӵ���һ��Ҫ��ƥ�����ӵ��Ǹ�node��
                    if eachKey in dictCurEntityPair:
                        # ��ʵ���൱�ڰ�dictResEntityPair��key������һ��node
                        dictResEntityPair[dictCurEntityPair[eachKey]] = dictResEntityPair[eachKey]

        # д����
        filePredicatePathSupSet.write(eachPath)
        for eachKey in dictResEntityPair:
            filePredicatePathSupSet.write('~')
            # һ������дvalue��ȥ��Ȼ����дkey����Ϊ���ӷ�ʽ
            filePredicatePathSupSet.write(dictResEntityPair[eachKey] + '\t' + eachKey)
        filePredicatePathSupSet.write('\n')

# ����candidate
for eachCandidate in dictPredicatePathCandidates:
    filePredicateCandidates.write(eachCandidate + '~' + dictPredicatePathCandidates[eachCandidate] + '\n')




cur.close()
conn.close()
filePredicateCandidates.close()
filePredicatePathSupSet.close()
fileCandidatePredicatePathForRep.close()

