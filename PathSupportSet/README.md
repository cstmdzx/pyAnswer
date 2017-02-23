# 生成候选谓语路径，同时还有候选谓语路径的支持集

- **GetEntityPairByPath.py 包含一个用来根据谓语路径从数据库中选出词对的函数，考虑了谓语的方向**
- **PathSupportSet.py 生成每个Path的支持集，集合中的每个元素为一个词对,输入为FilePredicatePath,输出为FilePredPathSupSet，以及FilePredPathAssociateRep**
- **FilePredPathSupSet 保存了谓语路径的支持集，format: Pred1[f/b]Pred2[f/b]...~PairX1	PairY1~PairX2	PairY2~...**
- **FilePredPathAssociateRep 与每个PredPath有关的RepId保存下来，后面计算相似度,format: Pred1[f/b]Pred2[f/b]...~RepId1~RepId2~...**
- **CandidatePredicatePathSupSet.py 这个是之前写的**
