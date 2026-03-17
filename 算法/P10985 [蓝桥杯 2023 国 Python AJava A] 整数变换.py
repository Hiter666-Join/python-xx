n = input()
cons = 0

while True:
    s = list(map(int, n))
    t = int(n) - sum(s)
    cons += 1
    if t == 0:
        break
    n = str(t)
print(cons)