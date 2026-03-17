a,b,n = map(int,input().split())
list1 = [a,a,a,a,a,b,b]
coun = 0
s = 0
while s < n:
    for i in list1:
        s += i
        coun += 1
        if s >= n:
            break
    if s >= n:
        break
print(coun)