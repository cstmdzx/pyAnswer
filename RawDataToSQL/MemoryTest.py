import sys

fileInstanceId = open('InstanceId', 'r')
filePredicateId = open('PredicateId', 'r')

dictInstance = dict()
dictPredicate = dict()

linesInstance = fileInstanceId.readlines()
linesPredicate = filePredicateId.readlines()

for eachInstance in linesInstance:
    eachInstance = eachInstance.replace('\n', '')
    words = eachInstance.split('\t')
    dictInstance[words[0]] = words[1]
    # print words[0]
    # print words[1]

print sys.getsizeof(dictInstance)

