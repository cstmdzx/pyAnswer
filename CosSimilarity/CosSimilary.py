# -*-coding:UTF-8-*-

# 计算Rep和Pred Path的余弦相似度
# 这里还需要计算所有词对的tf-idf

import math
from FuncEntityPairIdf import get_idf_by_file

def cos_similarity(dict_rep_pair, dict_pred_pair, str_rep, str_pred):
    # 计算余弦相似度
    # 输入为rep和pred词对idf的dict,以及两个的对应的向量字符串，format:pair1~pair2~...
    # 这里应该是没有包含Rep的id以及Pred的表达式

    words_rep = str_rep.split('~')
    words_pred = str_pred.split('~')

    float_rep_lenth = 0.0 # 计算vector_rep长度
    for each_pair in words_rep:
        float_rep_lenth += dict_rep_pair[each_pair] * dict_rep_pair[each_pair]

    float_pred_lenth = 0.0 # 计算vector_pred长度
    for each_pair in words_pred:
        float_pred_lenth += dict_pred_pair[each_pair] * dict_pred_pair[each_pair]

    float_similarity = 0.0 # 计算内积
    set_pred = set(words_pred)
    for each_pair in words_rep:
        if each_pair in set_pred:
            float_similarity += dict_rep_pair[each_pair] * dict_pred_pair[each_pair]

    float_similarity = float_similarity / sqrt(float_rep_lenth * float_pred_lenth)

    return float_similarity

def get_dict_by_file(file_dict_idf):
    # 专门用来处理FileDictIdf的，别的可能还得再写一个
    # 输入为dict_idf的文件句柄，输出为转化之后的dict
    lines_dict_idf = file_dict_idf.readlines()
    dict_idf = dict()
    for each_dict_idf in lines_dict_idf:
        each_dict_idf = each_dict_idf.replace('\n', '')
        words = each_dict_idf.split('\t')
        str_index = words[0]
        float_idf = float(words[1])
        dict_idf[str_index] = float_idf

    return dict_idf


if __name__ == '__main__':

    fileDictRepIdf = open('FileDictRepIdf', 'r')
    dictRepIdf = get_dict_by_file(fileDictRepIdf)
    fileDictPredIdf = open('FileDictPredIdf', 'r')
    dictPredIdf = get_dict_by_file(fileDictPredIdf)
    # 继续去处理，应该需要读取一个是包含PredPathAssociateRepId的那个文件，还有两个是分别的SupSet
    # 根据两个的SupSet,计算可能的candidate之间的相似度，就行了






