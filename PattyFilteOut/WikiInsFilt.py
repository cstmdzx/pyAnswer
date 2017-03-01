# -*-coding:UTF-8-*-

# 用来从patty-wiki-ins 中选出个数大于20的repid
# 注意修改两个地方，一个是if后面的条件，一个是文件名

def patty_filt_by_len(file_patty, int_len):
    dict_res = dict()
    lines_patty = file_patty.readlines()
    for each_patty in lines_patty:
        each_patty = each_patty.replace('\n', '')
        words = each_patty.split('\t')
        str_id = words[0]
        str_arg1 = words[1]
        str_arg2 = words[2]
        str_pair = str_arg1 + '\t' + str_arg2
        if str_id in dict_res:
            dict_res[str_id].append(str_pair)
        else:
            dict_res[str_id] = list()
            dict_res[str_id].append(str_pair)

    dict_res_final = dict()
    for each_key in dict_res:
        int_res_len = dict_res[each_key].__len__()
        if int_res_len < int_len:
            continue
        elif int_res_len > 150:
            continue
        else:
            dict_res_final[each_key] = dict_res[each_key]

    print dict_res_final.__len__()
    return dict_res_final

if __name__ == '__main__':
    filePatty = open('../patty-dataset/wikipedia-instances.txt', 'r')
    #filePattyAfter = open('wikipedia-instances-filt>8000', 'w')
    filePattyAfter = open('wikipedia-instances-filt100<<150', 'w')
    dictPatty = patty_filt_by_len(filePatty, 100)
    for eachId in dictPatty:
        listArg = dictPatty[eachId]
        for eachArg in listArg:
            filePattyAfter.write(eachId + '\t' + eachArg + '\n')

    filePatty.close()
    filePattyAfter.close()
