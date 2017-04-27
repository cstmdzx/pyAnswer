# -*-coding:UTF-8-*-

# shuchu top3

import operator

from paixu import CandSim
from random import sample


if __name__ == '__main__':
    dictPaixu = dict()

# ==============================================
    filePaixu = open('FilePaixuLen2<5', 'r')
    linesPaixu = filePaixu.readlines()

    for eachPaixu in linesPaixu:
        eachPaixu = eachPaixu.replace('\n', '')
        words = eachPaixu.split('\t')
        if words.__len__() < 3:
            continue
        strRepId = words[0]
        strPath = words[1]
        floatSim = float(words[2])
        if strRepId in dictPaixu:
            dictPaixu[strRepId].append(CandSim(strPath, floatSim))
        else:
            dictPaixu[strRepId] = list()
            dictPaixu[strRepId].append(CandSim(strPath, floatSim))

    filePaixu.close()

# ==============================================
    filePaixu = open('FilePaixuLen2100<<150', 'r')
    linesPaixu = filePaixu.readlines()

    for eachPaixu in linesPaixu:
        eachPaixu = eachPaixu.replace('\n', '')
        words = eachPaixu.split('\t')
        if words.__len__() < 3:
            continue
        strRepId = words[0]
        strPath = words[1]
        floatSim = float(words[2])
        if strRepId in dictPaixu:
            dictPaixu[strRepId].append(CandSim(strPath, floatSim))
        else:
            dictPaixu[strRepId] = list()
            dictPaixu[strRepId].append(CandSim(strPath, floatSim))

    filePaixu.close()

# ==============================================
    filePaixu = open('FilePaixu', 'r')
    linesPaixu = filePaixu.readlines()

    for eachPaixu in linesPaixu:
        eachPaixu = eachPaixu.replace('\n', '')
        words = eachPaixu.split('\t')
        if words.__len__() < 3:
            continue
        strRepId = words[0]
        strPath = words[1]
        floatSim = float(words[2])
        if strRepId in dictPaixu:
            dictPaixu[strRepId].append(CandSim(strPath, floatSim))
        else:
            # zheli bu tai yiyang
            continue

    filePaixu.close()

# ==============================================
    intPaixuLen = dictPaixu.__len__()
    listPaixuKey = dictPaixu.keys()
    listIntRand = sample(range(0, intPaixuLen), 100)
    fileRand100Top3 = open('FileRand100Top3', 'w')
    funcCmp = operator.attrgetter('Sim')
    for eachRand in listIntRand:
        strIndex = listPaixuKey[eachRand]
        listCand = dictPaixu[strIndex]
        listCand.sort(key=funcCmp, reverse=True)
        intFlag = min(listCand.__len__(), 3)
        for i in range(0, intFlag):
            fileRand100Top3.write(strIndex + '\t')
            fileRand100Top3.write(listCand[i].Cand + '\t' + str(listCand[i].Sim) + '\n')






