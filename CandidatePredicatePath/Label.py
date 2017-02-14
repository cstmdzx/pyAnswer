# -*-coding:UTF-8-*-

# 用来把所有谓语为<label>的subject以及他们对应的label找出来
# 统计程序运行时间

import time
import sys

if __name__ == '__main__':
    strPath = '../RawDataToSQL/'
    fileInstanceId = open(strPath + 'InstanceId')
    filePredicateId = open(strPath + 'PredicateId')
    linesInstanceId = fileInstanceId.readlines()
    linesPredicateId = filePredicateId.readlines()

    dictInstanceId = dict()
    dictPredicateId = dict()

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






