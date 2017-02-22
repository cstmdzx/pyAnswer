# -*-coding:UTF-8-*-
# 先生成一个O_SP试试，不行再想辙，行了就接着这条路走下去

import time

if __name__ == '__main__':
    print 'Start Reading File:'
    start = time.clock()
    fileSPO = open('./resSPO/SPO')
    linesSPO = fileSPO.readlines()


    print 'Finish Reading, Time: %f' % (time.clock() - start)
    fileS_OP = open('./resSPO/S_OP', 'w')
    fileP_SO = open('./resSPO/P_SO', 'w')
    fileO_SP = open('./resSPO/O_SP', 'w')
    fileOP_S = open('./resSPO/OP_S', 'w')
    fileSO_P = open('./resSPO/SO_P', 'w')
    fileSP_O = open('./resSPO/SP_O', 'w')

    intCount = 0
    for eachSPO in linesSPO:
        eachSPO = eachSPO.replace('\n', '')
        intCount += 1
        if intCount % 10000000 == 0: # total 250000000
            print time.clock() - start
        words = eachSPO.split('\t')
        # print words
        strSub = words[0]
        strPred = words[1]
        strObj = words[2]
        # print strSub
        # print strPred
        # print strObj
        if words.__len__() < 3:
            continue
        # fileS_OP.write(strSub + '\t' + strObj + '\t' + strPred + '\n')
        # fileP_SO.write(strPred + '\t' + strSub + '\t' + strObj + '\n')
        fileO_SP.write(strObj + '\t' + strSub + '\t' + strPred + '\n')
        # fileSO_P.write(strSub + '\t' + strObj + '\t' + strPred + '\n')
        # fileSP_O.write(strSub + '\t' + strPred + '\t' + strObj + '\n')
        # fileOP_S.write(strObj + '\t' + strPred + '\t' + strSub + '\n')

    print 'Finish Writing, Time: %f' % (time.clock() - start)
    fileS_OP.close()
    fileP_SO.close()
    fileO_SP.close()
    fileOP_S.close()
    fileSO_P.close()
    fileSP_O.close()
    print 'Finish Closing, Time: %f' % (time.clock() - start)

