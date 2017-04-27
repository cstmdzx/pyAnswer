# -*-coding:UTF-8-*-

# 计算Rep和Pred Path的余弦相似度
# 这里还需要计算所有词对的tf-idf

import math
from FuncEntityPairIdf import get_idf_by_file


def cos_similarity(dict_rep_pair_idf, dict_pred_pair_idf, list_rep, list_pred):
    # 计算余弦相似度
    # 输入为rep和pred词对idf的dict,以及两个的对应的向量字符串，format:pair1~pair2~...
    # 这里应该是没有包含Rep的id以及Pred的表达式
    '''
    words_rep = str_rep.split('~')
    words_pred = str_pred.split('~')
    '''

    #print 'changdu'
    float_rep_lenth = 0.0 # 计算vector_rep长度
    for each_pair in list_rep:
        #if each_pair not in dict_rep_pair_idf:
        #    print each_pair + 'not in rep_idf'
        #    continue
        float_rep_lenth += dict_rep_pair_idf[each_pair] * dict_rep_pair_idf[each_pair]

    float_pred_lenth = 0.0 # 计算vector_pred长度
    for each_pair in list_pred:
        #if each_pair not in dict_pred_pair_idf:
        #    print each_pair + 'not in pred_idf'
        #    continue
        float_pred_lenth += dict_pred_pair_idf[each_pair] * dict_pred_pair_idf[each_pair]

    float_similarity = 0.0 # 计算内积
    set_pred = set(list_pred)
    #print 'neiji'
    #print list_rep
    #print list_pred
    for each_pair in list_rep:
        if each_pair not in dict_rep_pair_idf:
            print each_pair + 'not in rep_idf'
            continue
        #if each_pair not in dict_pred_pair_idf:
        #    print each_pair + 'not in pred_idf'
        #    continue

        if each_pair in set_pred:
            float_similarity += dict_rep_pair_idf[each_pair] * dict_pred_pair_idf[each_pair]

    float_similarity = float_similarity / math.sqrt(float_rep_lenth * float_pred_lenth)

    return float_similarity


def get_dict_by_idf_file(lines_dict_idf):
    # 专门用来处理FileDictIdf的，别的可能还得再写一个
    # 输入为dict_idf的文件句柄，输出为转化之后的dict
    #lines_dict_idf = file_dict_idf.readlines()
    dict_idf = dict()
    for each_dict_idf in lines_dict_idf:
        each_dict_idf = each_dict_idf.replace('\n', '')
        words = each_dict_idf.split('~')
        if words.__len__() < 2:
            print 'len < 2'
            print words
            continue
        str_index = words[0]
        float_idf = float(words[1])
        dict_idf[str_index] = float_idf

    return dict_idf


def get_dict_by_supset_file(lines_file_supset):
    # 根据文件生成支持集词典
    # 输入为文件句柄，输出为向量dict，dict[id] = list[pair1, pair2, ...]
    #lines_file_supset = file_supset.readlines()
    dict_sup_vector = dict()

    for each_file_supset in lines_file_supset:
        each_file_supset = each_file_supset.replace('\n', '')
        words = each_file_supset.split('~')
        str_index = words[0]
        del words[0]
        dict_sup_vector[str_index] = list()
        for each_pair in words:
            words_pair = each_pair.split('\t')
            if words_pair.__len__() < 2:
                # print each_file_supset
                print words_pair
                continue
            dict_sup_vector[str_index].append(words_pair[0] + '\t' + words_pair[1])




    intFlag = 0
    for eachkey in dict_sup_vector:
        intFlag += 1
        print eachkey
        print dict_sup_vector[eachkey][0]
        if intFlag % 20 == 0:
            break


    return dict_sup_vector

if __name__ == '__main__':

    fileDictRepIdf = open('FileDictRepIdf', 'r')
    # dictRepIdf = get_dict_by_idf_file(fileDictRepIdf)
    fileDictPredIdf = open('FileDictPredIdf', 'r')
    # dictPredIdf = get_dict_by_idf_file(fileDictPredIdf)
    # 继续去处理，应该需要读取一个是包含PredPathAssociateRepId的那个文件，还有两个是分别的SupSet
    # 根据两个的SupSet,计算可能的candidate之间的相似度，就行了

    filePredPathSupSet = open('../PathSupportSet/PathRes/FilePredPathSupSetLen2100<<150', 'r')
    fileRepSupSet = open('FileRepSupSet', 'r')
    linesPredPathSupSet = filePredPathSupSet.readlines()
    linesRepSupSet = fileRepSupSet.readlines()

    dictPredPathSupSet = get_dict_by_supset_file(linesPredPathSupSet)
    dictRepSupSet = get_dict_by_supset_file(linesRepSupSet)
    dictRepIdf = get_idf_by_file(linesRepSupSet)
    dictPredIdf = get_idf_by_file(linesPredPathSupSet)

    #
    filePredPathAssocitedRep = open('../PathSupportSet/AssociateRes/FilePredPathAssociateRepLen2100<<150', 'r')
    linesPredPathAssocitedRep = filePredPathAssocitedRep.readlines()

    fileParaphraseDictionaryRepId = open('FileParaphraseDictionaryRepIdLen2100<<150', 'w') # format:strPredPath\t RepId\tfloatSimilarity\n
    for eachPredPathAssocitedRep in linesPredPathAssocitedRep:
        eachPredPathAssocitedRep = eachPredPathAssocitedRep.replace('\n', '')
        words = eachPredPathAssocitedRep.split('~')
        strPredPath = words[0]
        if strPredPath not in dictPredPathSupSet:
            continue
        del words[0]
        listRepId = words
        for eachRepId in listRepId:
            if eachRepId not in dictRepSupSet:
                continue
            floatSimilarity = cos_similarity(dictRepIdf, dictPredIdf, dictRepSupSet[eachRepId], dictPredPathSupSet[strPredPath])
            fileParaphraseDictionaryRepId.write(eachRepId + '\t' + strPredPath + '\t%f' % floatSimilarity + '\n')

    fileDictRepIdf.close()
    fileDictPredIdf.close()
    filePredPathSupSet.close()
    fileRepSupSet.close()
    filePredPathAssocitedRep.close()
    fileParaphraseDictionaryRepId.close()


