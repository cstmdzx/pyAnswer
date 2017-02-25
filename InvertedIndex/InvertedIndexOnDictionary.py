# coding=gbk
filePatterns = open('wikipedia-patterns.txt')  # <RelationPhraseId~predicate1[f/b]predicate2[f/b]predicate3[f/b],probability~……>
# filePatterns = open('test.txt')
fileInvertedIndex = open('InvertedIndex.txt', 'w')
linesDictionary = filePatterns.readlines()
del linesDictionary[0]

dictInvertedIndex = dict()

for eachLine in linesDictionary:
    words = eachLine.split('\t')
    strId = words[0]
    strPatterns = words[1]
    words2 = strPatterns.split(';$')
    intEnd = words2.__len__()
    del words2[intEnd - 1]
    for eachRelation in words2:
        words3 = eachRelation.split(' ')
        for eachWord in words3:
            # print eachWord
            if eachWord.find('[[') != -1 and eachWord.find(']]') != -1:
                continue
            else:
                if eachWord in dictInvertedIndex:
                    dictInvertedIndex[eachWord].add(strId)
                else:
                    dictInvertedIndex[eachWord] = set()
                    dictInvertedIndex[eachWord].add(strId)

for eachKey in dictInvertedIndex:
    '''
    print eachKey
    print dictInvertedIndex[eachKey]
    '''
    fileInvertedIndex.write(eachKey)
    for eachElement in dictInvertedIndex[eachKey]:
        fileInvertedIndex.write('~' + eachElement)
    fileInvertedIndex.write('\n')

fileInvertedIndex.close()
