#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
from datetime import date

def add_user(name: str,age: int):   #要导入的参数
    with pymysql.connect(           #配置数据库
        host='localhost',port=3306,user='root',
        password='123456',database='test_db',
        charset='utf8mb4') as conn:

        with conn.cursor() as cur:  #定义游标
            
            sql = "INSERT INTO users(name, age, created_at) VALUES (%s, %s, %s)"  #数据库操作
            cur.execute(sql,(name,age,date.today()))  #执行
            conn.commit()                             #提交
            print("插入成功，新id = ",cur.lastrowid)   #提示

if __name__ == '__main__':
    s,i = input().split()
    add_user(s,int(i))