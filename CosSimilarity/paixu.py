# -*-coding:UTF-8-*-

# paixu

import operator


class CandSim:
    def __init__(self, str_cand, float_sim):
        self.Cand = str_cand
        self.Sim = float_sim


if __name__ == '__main__':

    fileQuchong = open('FileQuchongLen2100<<150', 'r')
    linesQuchong = fileQuchong.readlines()
    dictRes = dict()

    for eachQuchong in linesQuchong:
        eachQuchong = eachQuchong.replace('\n', '')
        words = eachQuchong.split('\t')
        strIndex = words[0]
        strCand = words[1]
        floatSim = float(words[2])
        if strIndex in dictRes:
            dictRes[strIndex].append(CandSim(strCand, floatSim))
        else:
            dictRes[strIndex] = list()
            dictRes[strIndex].append(CandSim(strCand, floatSim))

    funcCmp = operator.attrgetter('Sim')

    for eachRes in dictRes:
        dictRes[eachRes].sort(key=funcCmp, reverse=True)

    filePaixu = open('FilePaixuLen2100<<150', 'w')
    for eachRes in dictRes:
        for eachCandSim in dictRes[eachRes]:
            filePaixu.write(eachRes + '\t' + eachCandSim.Cand + '\t' + str(eachCandSim.Sim) + '\n' )

    fileQuchong.close()
    filePaixu.close()


