# -*-coding:UTF-8-*-

# 这个没什么太多的用处，为了别的文件能够import这个文件夹里的.py
# 一些注释也写在这里，然后复制到vim里


# 周围第二圈
# 分开，取ins，这里的谓语是带着方向[f/b]的
# 删去第二圈里的回到出发点的ins，要不就出现一个环，错误的东西会越来越多
# 用来保存所有应该被删除的点的id
# len2里也是ins|pred[f/b]pred[f/b]
# 处理subject，筛出两层路径
# 处理object，同样的思路, 但是f和b要换以下，因为这次是从Obj出发的
# 一会回来改一下，分成四个文件来分别求
# 如果分开跑，Len2和Len3的地方得修改一下，整体一起跑就没事，dictObjLen1现在是在Len2上建的
# len1只需要SubLen1，len2需要SubLen1和ObjLen1，len3需要SubLen2和ObjLen1，len4需要SubLen2和ObjLen2

# 注意，结尾有可能是个‘.’，删了他
# 生成每个Path的支持集，集合中的每个元素为一个词对，这个集和可以被表示为一个向量
# 保存结果词对
# 读取之前的结果，这里保存的之前的候选路径
# 直接生成SPO的三元祖，考虑构建多列索引

# select ObjPred from (select Id from InstanceId where Ins = 'http://dbpedia.org/resource/Category:1989_albums') as a left outer join S_OP on a.Id = S_OP.Sub;
# select ObjPred from S_OP left outer join InstanceId on S_OP.Sub = InstanceId.Id where Ins = 'http://dbpedia.org/resource/Category:1989_albums'
# http://dbpedia.org/resource/Category:Softball_players
# select ObjPred from (select Id from InstanceId where Ins = 'http://dbpedia.org/resource/Category:Softball_players') as a left outer join S_OP on a.Id = S_OP.Sub; time:0.05sec
# select ObjPred from S_OP left outer join InstanceId on S_OP.Sub = InstanceId.Id where Ins = 'http://dbpedia.org/resource/Category:Softball_players'; time:

# 用来从dbpd_spo中选出非常要命的词对，
# 同时考虑了每个谓语的方向
# 这里没有考虑重复的问题，需要搞一个能查重的，重复的就不继续求了
# 这里没有记录每个path的对应的candidate，调用之前要搞一个
# 这里需要考虑下一次连接的时候，到底是主语还是宾语作为连接的条件
# 一共传递三个参数,index: 0.sql语句  1.这里谓语的方向  2.表格的temp名
# 好像没用了，因为有target和origine

# 先生成一个O_SP试试，不行再想辙，行了就接着这条路走下去
# 根据谓语路径，产生对应的词对
# 输入为每个谓语路径，返回结果为对应词对的list或者tuple，具体得看
# 去掉RepId,剩下的全是path
# 查出过匹配词对的就不再继续去匹配一遍了，匹配出的结果应该也写在硬盘上了
# 把与每个PredPath有关的RepId保存下来，后面计算相似度

# 这里还需要计算所有词对的tf-idf
# 把wiki-ins生成一个更好的文件，方便后面处理

# 用来生成每个词对的tf-idf，用于计算相似度
# 根据文件来生成词对的相似度
# 输入为文件句柄，输出为一个计算完成的词典

# 记录文档频率
