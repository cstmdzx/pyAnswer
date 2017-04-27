# -*-coding:UTF-8-*-

# quchong

from math import sqrt


if __name__ == '__main__':
    fileParaphraseDict = open('FileParaphraseDictionaryRepIdLen2100<<150', 'r')
    linesPara = fileParaphraseDict.readlines()
    dictRes = dict()
    setFlag = set()
    for eachPara in linesPara:
        eachPara = eachPara.replace('\n', '')
        words = eachPara.split('\t')
        strIndex = words[0]
        strCand = words[1]
        floatSim = float(words[2])
        if strIndex in dictRes:
            if strCand in dictRes[strIndex]:
                continue
            else:
                dictRes[strIndex][strCand] = sqrt(sqrt(floatSim))

        else:
            dictRes[strIndex] = dict()
            dictRes[strIndex][strCand] = sqrt(sqrt(floatSim))

    fileQuchong = open('FileQuchongLen2100<<150', 'w')
    for eachIndex in dictRes:
        for eachCand in dictRes[eachIndex]:
            if dictRes[eachIndex][eachCand] == 0.0:
                continue
            fileQuchong.write(eachIndex + '\t' + eachCand + '\t' + str(dictRes[eachIndex][eachCand]) + '\n')

    fileQuchong.close()


