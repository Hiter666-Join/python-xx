start = input().strip()
target = input().strip()

count = 0
s = list(start)

for i in range(len(s) - 1):
    if s[i] != target[i]:
        s[i] = 'o' if s[i] == '*' else '*'
        s[i + 1] = 'o' if s[i + 1] == '*' else '*'
        count += 1
print(count)