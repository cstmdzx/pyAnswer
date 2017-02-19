# -*-coding:UTF-8-*-

# 生成每个Path的支持集，集合中的每个元素为一个词对，这个集和可以被表示为一个向量

import MySQLdb
import re

import sys
sys.path.append('..')
from MySQLConn import mysql_conn


cur = mysql_conn()

if __name__ == '__main__':
    filePredicatePathSupSet = open('PredicatePathSupSet', 'w') # 保存结果词对
    filePredicatePath = open('FilePredicatePath', 'r') # 读取之前的结果, 这里保存的之前的候选路径
    filePredicateCandidates = open('PredicatePathCandidates', 'w') #

    linesPredicatePath = filePredicatePath.readlines()

    dictPredicatePathCandidates = dict()





