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
