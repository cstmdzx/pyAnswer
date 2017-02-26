# -*-coding:UTF-8-*-

# 用来生成paraphrase dictionary，并且排好序，返回的结果是一个排好序的dict

import operator

def class ParaDictItem:

    def __init__(self, path='', prob=0.0):
        self.str_path = path
        self.float_prob = prob

def get_ranked_para_dict(file_para_dict):
    # 输入是file，输出是排好序的dict
    # 问题的关键在于怎么把list排序
    # output format: dict[repid] = list(class(path, prob)), ranked by prob
    lines_para_dict = file_para_dict.readlines()
    dict_para_dict_ranked_by_prob = dict()

    # duru, goujian
    for each_para_dict in lines_para_dict:
        each_para_dict = each_para_dict.replace('\n', '')
        words_para_dict = each_para_dict.split('\t')
        if words_para_dict.__len__() != 3:
            print 'split error'
            print words_para_dict
            continue
        str_rep_id = words_para_dict[0]
        str_path = words_para_dict[1]
        str_prob = words_para_dict[2]
        if str_rep_id not in dict_para_dict_ranked_by_prob:
            dict_para_dict_ranked_by_prob[str_rep_id] = list()
        dict_para_dict_ranked_by_prob[str_rep_id].append( ParaDictItem(str_path, float(str_prob)) )

    # rank
    # cmp function
    funcCmpPathCand = operator.attrgetter('float_prob')
    for each_rep_id in dict_para_dict_ranked_by_prob:
        dict_para_dict_ranked_by_prob[each_rep_id].sort(key=funcCmpPathCand, reverse=True)

    return dict_para_dict_ranked_by_prob

if __name__ == '__main__':
    fileParaDict = open('../CosSimilarity/FileParaphraseDictionaryRepId', 'r')
    dictParaDictRankedByProb = get_ranked_para_dict(fileParaDict)





