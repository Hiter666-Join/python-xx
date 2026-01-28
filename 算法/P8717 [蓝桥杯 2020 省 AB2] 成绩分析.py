n = int(input())
list1 = []
for _ in range(n):
    s = int(input())
    list1.append(s)
print(max(list1))
print(min(list1))
a = sum(list1) / n
a1 = round(a,2)
print(a1)