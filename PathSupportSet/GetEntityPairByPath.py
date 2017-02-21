# -*-coding:UTF-8-*-

# 用来从dbpd_spo中选出非常要命的词对，
# 同时考虑了每个谓语的方向

import MySQLdb
import pdb

import sys
sys.path.append('..')
from MySQLConn import mysql_conn_name

cur = mysql_conn_name('dbpd_spo')


def get_entity_pair_by_path(str_path):
    # 这里没有记录每个path的对应的candidate，调用之前要搞一个
    words_pred_with_dir = str_path.split(']')
    list_sql_cmd = list()
    list_direct = list()
    int_temp_num = 0


    for each_pred_with_dir in words_pred_with_dir:
        int_temp_num += 1
        if each_pred_with_dir == '':
            continue
        words = each_pred_with_dir.split('[')
        str_pred = words[0]
        str_direct = words[1]
        print str_pred
        print str_direct
        str_sql_cmd = '(select Sub,Obj from SPO where Pred = ' + str_pred + ') as temp' + str(int_temp_num)
        list_sql_cmd.append([str_sql_cmd, str_direct, 'temp' + str(int_temp_num)])
        # 一共传递三个参数,index:  0.sql语句  1.这里谓语的方向  2.表格的temp名


    # pdb.set_trace()
    # 这里需要考虑下一次连接的时候，到底是主语还是宾语作为连接的条件
    list_previous = list_sql_cmd[0]
    del list_sql_cmd[0]
    str_sql_cmd_res = ''
    str_sql_cmd_res += list_previous[0]
    # str_origin = ''
    # str_target = ''

    if list_previous[1] == 'f':
        str_pre_origin = 'Sub'
        str_pre_target = 'Obj'
    else:
        str_pre_origin = 'Obj'
        str_pre_target = 'Sub'

    str_previous_tablename = ''
    str_cur_tablename = ''
    for each_sql_cmd in list_sql_cmd:
        int_temp_num += 1
        if each_sql_cmd[1] == 'f':
            str_cur_origin = str_previous_tablename + 'Sub'
            str_cur_target = str_previous_tablename + 'Obj'
        else:
            str_cur_origin = str_previous_tablename + 'Obj'
            str_cur_target = str_previous_tablename + 'Sub'

        str_select_item_origin = str_previous_tablename + str_pre_origin
        str_select_item_target = str_cur_tablename + str_cur_target
        str_on_item_target = str_previous_tablename + str_pre_target
        str_on_item_origin = str_cur_tablename + str_cur_origin


        str_sql_cmd_res = '(select ' +\
                list_previous[2] + '.' + str_select_item_origin + ' as ' +list_previous[2]+str_pre_origin + ',' +\
                each_sql_cmd[2] + '.' + str_select_item_target + 'as ' +each_sql_cmd[2]+str_cur_target +\
                ' from' +' (' + list_previous[0] + ' left outer join ' + each_sql_cmd[0] + \
                ' on ' + list_previous[2] + '.' + str_on_item_target + '=' + each_sql_cmd[2] + '.' + str_on_item_origin + ')) as ' +\
                'temp' + str(int_temp_num)
        # str_pre_origin = str_cur_origin
        str_previous_tablename = list_previous[2]
        str_cur_tablename = each_sql_cmd[2]
        str_pre_target = str_cur_target
        list_previous[0] = str_sql_cmd_res
        # list_previous[1] = # 好像没用了，因为有target和origin
        list_previous[2] = 'temp' + str(int_temp_num)

    print str_sql_cmd_res

    #if str_direct == 'f':

if __name__ == '__main__':

    get_entity_pair_by_path('pred1[f]pred2[b]pred3[f]pred4[b]')
'''
(select temp7.Obj,temp4.Subfrom
        (
            (select temp6.Obj,temp3.Objfrom
                (
                    (select temp1.Obj,temp2.Subfrom
                        (
                            (select Sub,Obj from SPO where Pred = pred1) as temp1left outer join
                            (select Sub,Obj from SPO where Pred = pred2) as temp2 on temp1.Sub=temp2.Obj)
                        ) as temp6left outer join
                    (select Sub,Obj from SPO where Pred = pred3) as temp3 on temp6.Sub=temp3.Sub)
                ) as temp7left outer join
            (select Sub,Obj from SPO where Pred = pred4) as temp4 on temp7.Obj=temp4.Obj
        )
        ) as temp8

(select temp7.Sub,temp4.Sub from
        (
            (select temp6.Sub,temp3.Obj from
                (
                    (select temp1.Sub,temp2.Sub from
                        (
                            (select Sub,Obj from SPO where Pred = pred1) as temp1 left outer join
                            (select Sub,Obj from SPO where Pred = pred2) as temp2 on temp1.Obj=temp2.Obj
                        )
                    ) as temp6 left outer join
                    (select Sub,Obj from SPO where Pred = pred3) as temp3 on temp6.Sub=temp3.Sub
                )
            ) as temp7 left outer join
            (select Sub,Obj from SPO where Pred = pred4) as temp4 on temp7.Obj=temp4.Obj
        )
) as temp8


'''
(select temp7.temp6Sub as temp7Sub,temp4.temp3temp6Subas temp4temp6Sub from
        (
            (select temp6.temp1Sub as temp6Sub,temp3.temp2temp1Objas temp3temp1Obj from
                (
                    (select temp1.Sub as temp1Sub,temp2.Subas temp2Sub from
                        (
                            (select Sub,Obj from SPO where Pred = pred1) as temp1 left outer join
                            (select Sub,Obj from SPO where Pred = pred2) as temp2 on temp1.Obj=temp2.Obj
                        )
                    ) as temp6 left outer join
                    (select Sub,Obj from SPO where Pred = pred3) as temp3 on temp6.temp1Sub=temp3.temp2temp1Sub
                )
            ) as temp7 left outer join
            (select Sub,Obj from SPO where Pred = pred4) as temp4 on temp7.temp6temp1Obj=temp4.temp3temp6Obj
        )
) as temp8
