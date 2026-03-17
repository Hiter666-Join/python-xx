#---------- 超时 ------------

def tsyear(year_list):
    coun = 0
    for y in year_list:
        list2 = list(map(int, y))
        if list2[0] == list2[2] and list2[3] - 1 == list2[1]:
            coun += 1
    return coun

list1 = []
for _ in range(5):
    n = input()
    list1.append(n)
result = tsyear(list1)
print(result)

# ---------------------------

def tsyear(year_list):
    coun = 0
    for y in year_list:
        if y[0] == y[2] and int(y[3]) - int(y[1]) == 1:
            coun += 1
    return coun

list1 = [input().strip() for _ in range(5)]
print(tsyear(list1))