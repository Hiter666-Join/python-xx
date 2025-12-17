#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def del_user(user_id: int):  #你要导入的参数
    with pymysql.connect(    #配置数据库
        host='localhost',port=3306,user='root',
        password='123456',database='test_db',
        charset='utf8mb4') as conn:

        with conn.cursor() as cur:                  #定义游标
            
            sql = "DELETE FROM users WHERE id = %s" #数据库操作
            cur.execute(sql,(user_id,))             #执行
            conn.commit()                           #提交
            print("删除行数 = ",cur.rowcount)        #提示

if __name__ == '__main__':
    del_user(input())  #删除id=X的内容