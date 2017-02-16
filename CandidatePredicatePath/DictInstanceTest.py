# -*-coding:UTF-8-*-

# 用来把所有instanceid以及predicateid插入到dict中，主要为了测试时间，结果在record中

import time
import sys

def IPToDict(dict_instance_id, dict_predicate_id):
    strPath = '../RawDataToSQL/'
    fileInstanceId = open(strPath + 'InstanceId')
    filePredicateId = open(strPath + 'PredicateId')
    linesInstanceId = fileInstanceId.readlines()
    linesPredicateId = filePredicateId.readlines()

    # dictInstanceId = dict()
    # dictPredicateId = dict()

    start = time.clock()

    for eachInstanceId in linesInstanceId:
        eachInstanceId = eachInstanceId.replace('\n', '')
        words = eachInstanceId.split('\t')
        if words.__len__() > 2:
            print 'error: duole'
        elif words.__len__() < 2:
            print 'error: shaole'

        strUri = words[0]
        strId = words[1]

        try:
            dictInstanceId[strUri] = strId
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print e
            print strUri
            print strId
            print eachInstanceId
            # continue

    mid = time.clock()
    print 'dict instance time:'
    print mid - start

    for eachPredicateId in linesPredicateId:
        eachPredicateId = eachPredicateId.replace('\n', '')
        words = eachPredicateId.split('\t')
        if words.__len__() > 2:
            print 'error: duole'
        elif words.__len__() < 2:
            print 'error: shaole'

        strUri = words[0]
        strId = words[1]

        try:
            dictPredicateId[strUri] = strId
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print e
            print strUri
            print strId
            print eachPredicateId

    end = time.clock()
    print 'dict predicate time:'
    print end - start



if __name__ == '__main__':
    dictInstanceId = dict()
    dictPredicateId = dict()

    IPToDict(dictInstanceId, dictPredicateId)

    for eachKey in dictInstanceId:
        print dictInstanceId[eachKey]







