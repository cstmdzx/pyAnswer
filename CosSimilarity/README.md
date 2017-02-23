# 计算Patty中relation phrase和Pred Path的相似度

- **CosSimilarity.py 计算余弦相似度**
- **FuncEntityPairIdf.py 用来生成每个词对的idf，用于计算相似度,返回值为计算完的dict[EntityPair] = idf，**
- **FileRepSupSet 保存的Rep的支持集，来自PattySupportSet.py, format: RepId~Pair1~Pair2~...**
- **PattySupportSet.py 把wiki-ins生成一个更好的文件，方便后面处理**
