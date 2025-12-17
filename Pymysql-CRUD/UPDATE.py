#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def update_age(user_id: int,new_age: int): #导入参数
    with pymysql.connect(   #配置数据库
        host='localhost',port=3306,user='root',
        password='123456',database='test_db',
        charset='utf8mb4') as conn:
        
        with conn.cursor() as cur: #定义游标

            sql = "UPDATE users SET age = %s WHERE id = %s"  #数据库操作
            cur.execute(sql,(new_age,user_id))  #执行
            conn.commit()                       #提交
            print("更改行数 = ",cur.rowcount)    #提示

if __name__ == '__main__':
    update_age(5,20)        #把id为X的用户年龄改为20岁