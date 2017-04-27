# -*-coding:UTF-8-*-

# 用来生成每个词对的idf，用于计算相似度

import math
import sys

def get_idf_by_file(lines_raw):
    # 根据文件来生成词对的tf-idf
    # 输入为文件句柄，输出为一个计算完成的词典
    # lines_raw = file_raw.readlines()
    dict_idf = dict()
    set_doc = set()

    for each_raw in lines_raw:
        each_raw = each_raw.replace('\n', '')
        words = each_raw.split('~')
        str_index = words[0]
        del words[0]
        for each_entity_pair in words:
            # 记录文档频率
            if each_entity_pair not in dict_idf:
                dict_idf[each_entity_pair] = 1
            else:
                dict_idf[each_entity_pair] += 1

        if str_index not in set_doc:
            set_doc.add(str_index)

    int_doc_num = set_doc.__len__()
    # --------------calculate idf using log-------------
    for each_key in dict_idf:
        try:
            dict_idf[each_key] = math.log10(int_doc_num / dict_idf[each_key])
        except Exception as e:
            print e
            print int_doc_num
            print dict_idf[each_key]
            continue
        except KeyboardInterrupt:
            sys.exit(0)

    return dict_idf

if __name__ == '__main__':

    fileRepSupSet = open('FileRepSupSet', 'r')
    dictRepIdf = get_idf_by_file(fileRepSupSet)
    fileDictRepIdf = open('FileDictRepIdf', 'w')
    for eachKey in dictRepIdf:
        fileDictRepIdf.write(eachKey + ('~%f' % dictRepIdf[eachKey]) + '\n')
    '''
    # a print test
    intFlag = 0
    for eachKey in dictRepIdf:
        print ('%s : %f') % (eachKey, dictRepIdf[eachKey])
        intFlag += 1
        if intFlag % 10 == 0: break
    '''

    # FilePredSupSet unfinish
    filePredSupSet = open('../PathSupportSet/PathRes/FilePredPathSupSetLen1', 'r')
    dictPredIdf = get_idf_by_file(filePredSupSet)
    fileDictPredIdf = open('FileDictPredIdf', 'w')
    for eachKey in dictPredIdf:
        fileDictPredIdf.write(eachKey + ('~%f' % dictPredIdf[eachKey]) + '\n')



