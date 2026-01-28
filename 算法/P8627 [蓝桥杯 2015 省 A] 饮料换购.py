n = int(input())
total = n
caps = n
while caps >= 3:
    exchanged = caps // 3
    total += exchanged
    caps = caps % 3 + exchanged
print(total)