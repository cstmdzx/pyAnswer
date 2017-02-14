# 用来把rdf中的所有主谓宾转换成id
### InstanceId 所有实例转化的结果，包括主语和宾语
### PredicateId 所有谓语转化的结果
### MemoryTest.py 本来想用来测试把InstanceId做成一个dict要用多大内存，但是好像出问题了，结果是个指针的大小
### MySQLTest.py 之前采用hash策略的将主语谓语宾语插入到mysql中的程序
### RawDataProcess.py 处理数据，好像是还没写完，生成结果的，把rdf生成S_OP那一堆
### /res 结果，里面存的数据处理结果，github上没传，太大了
