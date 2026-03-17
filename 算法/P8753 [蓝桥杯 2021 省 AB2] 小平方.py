def jiego(n):
    list1 = [i for i in range(1,n) if i**2%n < n/2]
    print(len(list1))

s = int(input())
jiego(s)