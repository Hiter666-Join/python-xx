
import os
import sys
from time import sleep

students_dict = {} #用字典来装学生的信息，以key为班级和学号来存放，方便查找

def qinli():
    os.system('cls' if os.name == 'nt' else 'clear')    #清屏，并且判断系统是win还是linux/macOS

def tiaopin():
    sleep(1)
    qinli()

def fonmian():  #程序封面
    print("欢迎进入学生系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查找学生信息")
    print("0.退出系统")

def main(): #程序进入
    
    while True: #使用循环，让程序持续接受输入，程序的可持续使用
        fonmian()
        xz = int(input("输入号码进入对应功能:"))

        if xz == 1:
            add_students()
        elif xz == 2:
            delete_students()
        elif xz == 3:
            edit_students()
        elif xz == 4:
            search_students()
        elif xz == 0:
            sys.exit(0) #用break也可以退出循环
        else:   #注意输入的限制
            print("输入有误")

# 添加功能
def add_students():
    name = input("输入你的名字：")
    age = input("输入你的年龄：")
    stu_class = input("输入你的班级：")
    number = input("输入你的学号：")
    Key = (stu_class,number)
    if Key in students_dict:    #判断一下这个学生是否存在，避免反复添加
        print("该学生已经存在")
        tiaopin()
    else:
        new_dict = dict()   #建立一个字典来存放学生信息
        new_dict['name'] = name
        new_dict['age'] = age
        new_dict['stu_class'] = stu_class
        new_dict['number'] = number
        students_dict[(stu_class,number)] = new_dict    #把new_dict字典存放的信息以key为班级和学号的方式放入到students_dict
        print("添加成功！")
        tiaopin()

# 删除功能
def delete_students():
    delrte_class = input("输入你要删除的学生班级：")
    delrte_number = input("输入你要删除的学生学号：")
    Key = (delrte_class,delrte_number)

    lookin = students_dict.get(Key)
    if lookin:
        print(f"该学生的名字是：{lookin['name']}，这个学生的年龄是：{lookin['age']}")
        judgment = input("是否要删除该学生信息（Y/N）：")
        if judgment.lower() == 'y': #lower()把字符大小写统一为小写
            del students_dict[Key]
            print("删除成功！")
            tiaopin()
        else:
            print("输入错误")
            tiaopin()
    else:
        print("这个学生信息不存在")
        tiaopin()

# 修改功能
def edit_students():
    edit_class = input("输入你要修改的学生班级：")
    edit_number = input("输入你要修改的学生学号：")
    Key =(edit_class,edit_number)

    lookin = students_dict.get(Key)
    if lookin:
        print(f"该学生的名字是：{lookin['name']}，年龄是：{lookin['age']}")
        judgment = input("是否要修改该学生信息（Y/N）：")
        if judgment.lower() == 'y':
            new_name = input("请输入修改的名字：")
            new_age = input("请输入修改的年龄：")
            lookin['name'] = new_name
            lookin['age'] = new_age
            print(f"修改完成！修改效果：该学生的名字是：{lookin['name']},年龄是{lookin['age']},班级是{edit_class},学号是{edit_number}")
            input("输入回车返回页面：")
            tiaopin()
        else:
            print("输入错误")
            tiaopin()
    else:
        print("输入的信息不存在")
        tiaopin()

# 查找功能    
def search_students():
    if len(students_dict) != 0:
        print("学生信息如下：")
        for (cls,num),student in students_dict.items():
            print(f"学生姓名是{student['name']},年龄是{student['age']},班级是{cls},学号是{num}")
        input("输入回车返回页面：")
        tiaopin()
    else:
        print("学生信息不存在")
        tiaopin()

if __name__ == "__main__":
    main()