def F(n, lists):
    if n < len(lists) and lists[n]:
        return lists[n]
    if n % 2 == 0:
        nxt = n // 2
    else:
        nxt = n * 3 + 1
    peak = max(n, F(nxt, lists))
    if n < len(lists):
        lists[n] = peak
    return peak

N = int(input())
lists = [0] * (N + 1)
lists[1] = 1
ans = 0
for i in range(1, N + 1):
    ans = max(ans, F(i, lists))
print(ans)