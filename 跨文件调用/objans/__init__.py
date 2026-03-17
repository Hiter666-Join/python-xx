from . import main  #form . import XXX 相对导入，就是基于该目录下导入
from .main import x

__all__ = ["main","x"]  #管理open.py的import * 的内容，这里放入了main.py的main方法和定义的x参数

print("__init__ say hello")