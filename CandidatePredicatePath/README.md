# 选出每一个RelationPhrase的候选Predicate/Path
- **DictInstanceTest.py 用来把所有instanceid以及predicateid插入到dict中，主要为了测试时间，结果在record中**
- **GetIdByUrl.py 包含两个主要函数，用来从数据库中找ins以及Pred的Id** 
- **GetValueByIndex.py 包含从S_OP中根据OP选S和根据S选OP的，以及其他几张表(P_SO,O_SP)，同类的函数**
- **__init__.py 为了别的文件能够import这个文件夹里的.py**
- **CandidatePredicatePath.py 生成关系词的候选谓语路径**
- **record 记录DictInstanceTest.py的测试时间结果,以及len1的时间**
- **CandidatePredicatePathForRep.py和CandidatePredicatePathForRep2.py是之前写的，目前主要有用的还是CandidatePredicatePath.py**
- **/FilePredicatePath/ 里保存的PredicatePath，从CandidatePredicatePath.py里的出来的，里面有len1234，没有上传到github，太大了**
