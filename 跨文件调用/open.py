import main2    #调用main2.py
from objans import *    #import objans会调用目录下的__init__.py

print(x)    #x是objans目录下的main.py的参数
main2.main2()   #使用main2.py的main2()方法
print(main.x)   #调用objans目录下的main.py的x参数
main.say_bye()  #调用objans目录下的main.py的say_bye方法