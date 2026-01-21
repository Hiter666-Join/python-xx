n = int(input())
list1 = [n]
while n > 1:
    n //= 2
    list1.append(n)
print(' '.join(map(str,list1)))