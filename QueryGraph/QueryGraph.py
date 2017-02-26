# -*-coding:UTF-8-*-

# 生成查询图，包括抽出关系词，合并并且抽出关系词

import re

from pygraph.classes.graph import graph
from pygraph.algorithms.searching import depth_first_search_return_by_rep
from FuncGetRankedParaDict import get_ranked_para_dict
from FuncGetDictRepSplitWord import get_dict_rep_split_word

if __name__ == '__main__':

    fileParaDict = open('../CosSimilarity/FileParaphraseDictionaryRepId', 'r')
    dictParaDictRankedByProb = get_ranked_para_dict(fileParaDict)

    fileDepTree = open('FileDependencyTree', 'r')
    linesDepTree = fileDepTree.readlines()

    patternNode = re.compile(r'(.+)\((.+)-(\d),\s(.+)-(\d)\)')

    #
    graphDepTree = graph()
    for eachDepTree in linesDepTree:
        eachDepTree = eachDepTree.replace('\n', '')
        wordsDepTree = eachDepTree.split('~')
        for eachRelation in wordsDepTree:
            nodes = patternNode.search(eachRelation)
            strEdgeLabel = nodes.group(1)
            strNode1Label = nodes.group(2)
            intNode1Id = nodes.group(3)
            strNode2Label = nodes.group(4)
            intNode2Id = nodes.group(5)
            try:
                graphDepTree.add_node(node=intNode1Id)
            except:
                print 'Node %s already in graph' % intNode1Id

            try:
                graphDepTree.add_node(node=intNode2Id)
            except:
                print 'Node %s already in graph' % intNode2Id

            try:
                graphDepTree.add_edge(edge=(intNode1Id, intNode2Id), label=strEdgeLabel)
            except:
                "Edge (%d, %d) already in graph" % (intNode1Id, intNode2Id)

        # dfs
        fileInvertedIndex = open('../InvertedIndex/FileInvertedIndex.txt', 'r')
        dictRepSplitWord = get_dict_rep_split_word(fileInvertedIndex)

        listRepByDFS = list() # format:((listRepPath0, setRepId), (listRepPath0, setRepId), ...)
        for eachNode in graphDepTree.nodes():
            dictSpanningTree, listPre, listPost, setRepId, listRepPath = depth_first_search_return_by_rep(graphDepTree, root=eachNode, fileter=null(), dict_rep_split_word=dictRepSplitWord)
            if setRepId.__len__() == 0:
                continue
            listRepPath0 = listRepPath[0]
            listRepByDFS.append((listRepPath0, setRepId))

        # generate query graph
        setSubLikeLabel = {} # need to be defined
        setObjLikeLabel = {} # need to be defined
        dictPathCorRepId = dict()
        for eachPathSetPair in listRepByDFS:
            listPath = eachPathSetPair[0]
            setRep = eachPathSetPair[1]
            strPathIndex = ''
            for eachWord in listPath:
                strPathIndex += eachWord
            dictPathCorRepId[strPathIndex] = setRep

        for eachRepPath in listRepByDFS:
            listPath = eachRepPath[0]
            for eachWord in listPath:
                listNeighbors









