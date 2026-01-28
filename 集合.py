set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# 查询集合中元素
print(f"1在不在set1中:{1 in set1}")
print(f"1在不在set2中:{1 in set2}")

# 获取集合长度
print(f"set1的集合长度是:{len(set1)}")
print(f"set2的集合长度是:{len(set2)}")

# 返回一个包含所有元素的新集
print(f"并集是:{set1 | set2}")

# 返回一个包含共有元素的新集
print(f"交集是:{set1 & set2}")

# 返回一个只出现在set1里的新集
print(f"set1相对set2的差集:{set1 - set2}")

# 询问set1元素是否都在set2中
print(f"set1是否都在set2中:{set1 <= set2}")

# 返回一个包含set1和set2所有元素的集
print(f"set1和set2的并集:{set1.union(set2)}")

# 返回一个两个集共有元素的集
print(f"set1和set2的交集:{set1.intersection(set2)}")

# 返回一个只出现在set1里的集
print(f"set1对于set2的差集:{set1.difference(set2)}")

# 询问set1是否是set2的子集
print(f"set1是否是set2的子集:{set1.issubset(set2)}")

# 添加一个元素
set1.add(6)
print(f"添加一个6后:{set1}")

# 移除一个元素
set1.remove(1)
print(f"移除一个1后:{set1}")

# 随机移除一个元素
set1.pop()
print(f"随机删除一个元素后:{set1}")

# 清除全部元素
set1.clear()
print(f"清除全部元素后:{set1}\n注:{{}}是字典的空表达,set()是集合的空表达")