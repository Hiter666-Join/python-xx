#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def list_users():  #无导入参数
    with pymysql.connect(   #配置数据库
        host='localhost',port=3306,user='root',
        password='123456',database='test_db',
        charset='utf8mb4') as conn:

        with conn.cursor(pymysql.cursors.DictCursor) as cur:  #定义游标  pymysql.cursors.DictCursor后会把读取元组变成读取字典
            
            cur.execute("SELECT id, name, age, created_at FROM users ORDER BY id DESC")  #数据库操作
            rows = cur.fetchall()   #获取全部数据库内容

            for r in rows:
                print(r)        #循环输出内容

if __name__ == '__main__':
    list_users()