a = int(input())
s = 0
h = 0
while s != a:
    s += 1
    l = list(str(s))
    s1 = l.count("1")
    s2 = l.count("2")
    s9 = l.count("9")
    s0 = l.count("0")
    if s1 or s2 or s9 or s0 > 0 :
        h += s
print(h)