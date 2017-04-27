# -*-coding:UTF-8-*-

# 生成关系词的候选谓语路径
# 长度暂时计划不超过5
# 先从1开始，然后递增: 1,2,4……
# 结果保存在文件FileCandidatePredicatePath中，格式为：RelationPhraseId~Predicate[f/b]Predicate[f/b]…­~Predicate[f/b]Predicate[f/b]…

# 如果分开跑，Len2和Len3的地方得修改一下，整体一起跑就没事，dictObjLen1现在是在Len2上建的

import MySQLdb
import time

import sys
sys.path.append('..')

from Lib.FuncVirtuosoConn import get_query_results
from FuncGetSparqlByLen import get_sparql_by_len
from FuncGetSparqlByLen import get_sparql_by_len_with_label

if __name__ == '__main__':
    fileWikiIns = open('../PattyFilteOut/wikipedia-instances-filt100<<150', 'r')
    start = time.time()
    linesWikiIns = fileWikiIns.readlines()
    print 'Read Wiki Ins Finish'
    print 'Read Time %f' % (time.time()-start)

    fileRes = open('FileCandidatePredicatePath', 'w')
    strResPath = './FilePredicatePath/'
    #filePredPathLen1 = open(strResPath + 'Len1', 'w')
    #filePredPathLen2 = open(strResPath + 'Len2_2nd', 'w')
    filePredPathLen3 = open(strResPath + 'Len3', 'w')
    #filePredPathLen4 = open(strResPath + 'Len4', 'w')

    fileRecord = open('record', 'a')

    intFlag = 0


    for eachWikiIns in linesWikiIns:
        intFlag += 1
        if intFlag % 100 == 0:
            print intFlag
            print time.time() - start

        # diyici bengkui de difang

        #if intFlag < 51300:
        #    continue

        #

        eachWikiIns = eachWikiIns.replace('\n', '')
        words = eachWikiIns.split('\t')
        if words.__len__() < 3:
            continue

        strRepId = words[0]
        # fileRes.write(strRepId)
        # filePredPathLen2.write(strRepId)
        # filePredPathLen3.write(strRepId)
        # filePredPathLen4.write(strRepId)

        strRepSub = words[1]
        strRepSub = strRepSub.replace('\"', '\\"')
        #strRepSub = strRepSub.replace('\'', '\\\'')
        strRepSub = '\"' + strRepSub + '\"@en'
        strRepObj = words[2]
        strRepObj = strRepObj.replace('\"', '\\"')
        #strRepObj = strRepObj.replace('\'', '\\\'')
        strRepObj = '\"' + strRepObj + '\"@en'
         # 一会回来改一下，分成四个文件来分别求
        # len 1
        '''

        #print 'Before Get Sparql: %f' % (time.time() - start)
        listSparqlLen1 = get_sparql_by_len(strRepSub, strRepObj, 1)
        #print 'After Get Sparql: %f' %  (time.time() - start)
        for eachItem in listSparqlLen1:
            strSparqlCmd, tupleDir = eachItem
            #print 'Before Query: %f' % (time.time() - start)
            #print strSparqlCmd
            listPathLen1 = get_query_results(strSparqlCmd)
            try:
                listPathLen1 = get_query_results(strSparqlCmd)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                print e
                print strSparqlCmd
                continue
            #print 'After Query: %f' % (time.time() - start)

            if listPathLen1.__len__() == 0:
                continue
            filePredPathLen1.write(strRepId)
            for eachDictItem in listPathLen1:
                # print eachDictItem['p1'] + tupleDir[0]
                try:
                    strWrite = '~' + eachDictItem['p1'] + tupleDir[0]
                    filePredPathLen1.write(strWrite.encode('utf-8'))
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    print e
                    print '~' + eachDictItem['p1'] + tupleDir[0]
                    print type('~' + eachDictItem['p1'] + tupleDir[0])
            filePredPathLen1.write('\n')

        #print 'After A WikiIns Line Query: %f' % (time.time() - start)

        '''

        # len 2 , zhu yao jiushi zhege
        #listSparqlLen2 = get_sparql_by_len(strRepSub, strRepObj, 2)
        #for eachItem in listSparqlLen2:
        #    strSparqlCmd, tupleDir = eachItem
        #    tempStart = time.time()
        #    intSparqlCmdLen = strSparqlCmd.__len__()
        #    strSparqlCmd = strSparqlCmd[:intSparqlCmdLen - 2]
        #    strSparqlCmd += 'FILTER (?p1 != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>) }'
        #    # strSparqlCmd = strSparqlCmd.replace('select', 'select distinct')

        #    # print strSparqlCmd
        #    try:
        #        listPathLen2 = get_query_results(strSparqlCmd)
        #    except Exception as e:
        #        print e
        #        print strSparqlCmd
        #        continue
        #    except KeyboardInterrupt:
        #        sys.exit(0)
        #    #print time.time() - tempStart
        #    '''
        #    if (time.time()-tempStart) > 0.5:
        #        print strSparqlCmd
        #        print listPathLen2
        #    '''
        #    # print listPathLen2
        #    if listPathLen2.__len__() == 0:
        #        continue
        #    # print strSparqlCmd
        #    filePredPathLen2.write(strRepId)
        #    for eachDictItem in listPathLen2:
        #        try:
        #            filePredPathLen2.write(('~' + eachDictItem['p1'] + tupleDir[0]).encode('utf-8'))
        #            filePredPathLen2.write((eachDictItem['p2'] + tupleDir[1]).encode('utf-8'))
        #        except KeyboardInterrupt:
        #            sys.exit(0)
        #        except Exception as e:
        #            print e
        #            print strSparqlCmd
        #            # print listPathLen2
        #            print eachDictItem
        #            print '~' + eachDictItem['p1'] + tupleDir[0]
        #            print '~' + eachDictItem['p2'] + tupleDir[1]
        #            print type('~' + eachDictItem['p1'] + tupleDir[0])
        #            print type('~' + eachDictItem['p2'] + tupleDir[1])


        #    filePredPathLen2.write('\n')


        # len 3
        listSparqlLen3 = get_sparql_by_len_with_label(strRepSub, strRepObj, 3)
        for eachItem in listSparqlLen3:
            strSparqlCmd, tupleDir = eachItem
            tempStart = time.time()
            #intSparqlCmdLen = strSparqlCmd.__len__()
            #strSparqlCmd = strSparqlCmd[:intSparqlCmdLen - 2]
            #strSparqlCmd += 'FILTER (?p1 != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> and ?p2 != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>) }'
            # strSparqlCmd = strSparqlCmd.replace('select', 'select distinct')

            # print strSparqlCmd
            try:
                listPathLen3 = get_query_results(strSparqlCmd)
            except Exception as e:
                print e
                print strSparqlCmd
                continue
            except KeyboardInterrupt:
                sys.exit(0)
            #print time.time() - tempStart
            '''
            if (time.time()-tempStart) > 0.5:
                print strSparqlCmd
                print listPathLen3
            '''
            # print listPathLen3
            if listPathLen3.__len__() == 0:
                continue
            # print strSparqlCmd
            filePredPathLen3.write(strRepId)
            for eachDictItem in listPathLen3:
                try:
                    filePredPathLen3.write(('~' + eachDictItem['p1'] + tupleDir[0]).encode('utf-8'))
                    filePredPathLen3.write((eachDictItem['p2'] + tupleDir[1]).encode('utf-8'))
                    filePredPathLen3.write((eachDictItem['p3'] + tupleDir[2]).encode('utf-8'))
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    print e
                    print strSparqlCmd
                    # print listPathLen3
                    print eachDictItem
                    print '~' + eachDictItem['p1'] + tupleDir[0]
                    print '~' + eachDictItem['p2'] + tupleDir[1]
                    print '~' + eachDictItem['p3'] + tupleDir[2]
                    print type('~' + eachDictItem['p1'] + tupleDir[0])
                    print type('~' + eachDictItem['p2'] + tupleDir[1])
                    print type('~' + eachDictItem['p3'] + tupleDir[2])


            filePredPathLen3.write('\n')


        '''
        listSparqlLen3 = get_sparql_by_len(strRepSub, strRepObj, 3)
        for eachItem in listSparqlLen3:
            strSparqlCmd, tupleDir = eachItem
            listPathLen3 = get_query_results(strSparqlCmd)
            if listPathLen3.__len__() == 0:
                continue
            filePredPathLen3.write(strRepId)
            for eachDictItem in listPathLen1:
                filePredPathLen3.write('~' + eachDictItem['p1'] + tupleDir[0])
                filePredPathLen3.write('~' + eachDictItem['p2'] + tupleDir[1])
                filePredPathLen3.write('~' + eachDictItem['p3'] + tupleDir[2])
            filePredPathLen3.write('\n')
        '''

        # len 4
        '''
        listSparqlLen4 = get_sparql_by_len(strRepSub, strRepObj, 4)
        for eachItem in listSparqlLen4:
            strSparqlCmd, tupleDir = eachItem
            listPathLen4 = get_query_results(strSparqlCmd)
            if listPathLen4.__len__() == 0:
                continue
            filePredPathLen4.write(strRepId)
            for eachDictItem in listPathLen1:
                filePredPathLen4.write('~' + eachDictItem['p1'] + tupleDir[0])
                filePredPathLen4.write('~' + eachDictItem['p2'] + tupleDir[1])
                filePredPathLen4.write('~' + eachDictItem['p3'] + tupleDir[2])
                filePredPathLen4.write('~' + eachDictItem['p4'] + tupleDir[3])
            filePredPathLen4.write('\n')
        '''


    end = time.time()
    print 'Time: %f' % (end-start)
    fileRecord.write('Time: %f' % (end-start))
    #cur.close()
    fileRes.close()
    #filePredPathLen1.close()
    #filePredPathLen2.close()
    filePredPathLen3.close()
    #filePredPathLen4.close()
    fileWikiIns.close()

