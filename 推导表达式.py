# 列表推导式
old_list:list[int] = [1,2,3,4,5,6,7,8,9,10]
new_list = [i for i in old_list if i % 2 == 0]
print(new_list)

# 集合推导式
new_str = {i for i in old_list if i % 2 == 0}
print(new_str)

# 字典推导式
new_dict = {i:i**2 for i in old_list}
print(new_dict)

# 双循环推导式
strs:list[str] = ["flower","for","flounder"]
chars = [ch for s in strs for ch in s]
print(chars)