import sys
import pydblite
import time

intStartTime = time.time()

strFilePath = '../RawDataToSQL/'

pydb = pydblite.Base(':memory:')
pydb.create('Url', 'Id')

fileInstanceId = open(strFilePath + 'InstanceId', 'r')
linesInstanceId = fileInstanceId.readlines()
print linesInstanceId.__len__()
intCount = 0
for eachInstanceId in linesInstanceId:
    eachInstanceId = eachInstanceId.replace('\n', '')
    words = eachInstanceId.split('\t')
    strUrl = words[0]
    strInstanceId = words[1]
    pydb.insert(Url = strUrl, Id = strInstanceId)
    intCount += 1
    if intCount % 10000 == 0:
        print intCount

print 'insert finish'
intTime = time.time()
print 'insert time: ' + str(intTime - intStartTime)

pydb.create_index('Url')

intEndTime = time.time()
print 'create index time:' + str(intEndTime - intStartTime)

print sys.getsizeof(pydb)


