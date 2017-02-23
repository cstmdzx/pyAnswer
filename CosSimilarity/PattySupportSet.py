# -*-coding:UTF-8-*-

# 把wiki-ins生成一个更好的文件，方便后面处理

import sys
import time

if __name__ == '__main__':

    filePattyWikiIns = open('../patty-dataset-freebase/wikipedia-instances.txt', 'r')
    linesPattyWikiIns = filePattyWikiIns.readlines()

    fileRepSupSet = open('FileRepSupSet', 'w')

    dictRepSupSet = dict()

    for eachPattyWikiIns in linesPattyWikiIns:
        eachPattyWikiIns = eachPattyWikiIns.replace('\n', '')
        words = eachPattyWikiIns.split('\t')

        if words.__len__() < 3:
            continue

        strRepId = words[0]
        strEntityPair = words[1] + '\t' + words[2]

        if strRepId not in dictRepSupSet:
            dictRepSupSet[strRepId] = strEntityPair
        else:
            dictRepSupSet[strRepId] += '~' + strEntityPair

    for eachKey in dictRepSupSet:
        fileRepSupSet.write(eachKey + '~' + dictRepSupSet[eachKey] + '\n')

    fileRepSupSet.close()
    filePattyWikiIns.close()





