# 将自然语言生成查询图，再生成sparql

- **FileQuestion 用来存要测试的问题**
- **FileDependencyTree 利用stanford parser生成的依赖树，这个是用java程序跑的**
- **QueryGraph.py 生成查询图，包括抽出关系词，合并并且抽出关系词**
- **FuncGetRankedParaDict.py 用来生成paraphrase dictionary，并且排好序，返回的结果是一个排好序的dict**
- **需要安装[python-graph](https://pypi.python.org/pypi/python-graph)**
- **FuncGetDictRepSplitWord.py 用来把之前处理出来的InvertedIndex生成一个dict，感觉这个有点多此一举，但是之前生成保存的时候那个代码有点看不明白了……**

