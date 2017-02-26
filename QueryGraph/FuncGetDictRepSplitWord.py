# -*-coding:UTF-8-*-

# 用来把之前处理出来的InvertedIndex生成一个dict

def get_dict_rep_split_word(file_inverted_index):
    lines_inverted_index = file_inverted_index.readlines()
    dict_rep_split_word = dict()

    for each_inverted_index in lines_inverted_index:
        each_inverted_index = each_inverted_index.replace('\n', '')
        words_inverted_index = each_inverted_index.split('~')
        str_word = words_inverted_index[0]
        del words_inverted_index[0]
        set_related_rep_id = set()
        for each_rep_id in words_inverted_index:
            set_related_rep_id.add(each_rep_id)

        dict_rep_split_word[each_inverted_index] = set_related_rep_id

    return dict_rep_split_word


if __name__ == '__main__':

    fileInvertedIndex = open('../InvertedIndex/FileInvertedIndex.txt', 'r')
    dictRepSplitWord = get_dict_rep_split_word(fileInvertedIndex)
