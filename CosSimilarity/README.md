# 计算Patty中relation phrase和Pred Path的相似度

- **CosSimilarity.py 计算余弦相似度,最终生成词典FileParaphraseDictionaryRepId**
- **FuncEntityPairIdf.py 用来生成每个词对的idf，用于计算相似度,返回值为计算完的dict[EntityPair] = idf，**
- **FileRepSupSet 保存的Rep的支持集，来自PattySupportSet.py, format: RepId~Pair1~Pair2~...**
- **PattySupportSet.py 把wiki-ins生成一个更好的文件，方便后面处理**
- **FileParaphraseDictionaryRepId 基本上就是ParaphraseDictionary，但是Rep是id，可能还需要再生成一步，把Id换成真正的Rep,不过也不一定，可以在生成查询图的时候根据文件查Id,由于还查一个输入文件，现在还没跑，跑完也不会传到github，太大了……**
