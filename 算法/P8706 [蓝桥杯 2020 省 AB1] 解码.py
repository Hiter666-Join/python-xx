s = input()
result = []
i = 0
while i < len(s):
    if s[i].isalpha():
        result.append(s[i])
        i += 1
    elif s[i].isdigit():
        digit = int(s[i])
        prev_char = result[-1]
        result.extend([prev_char] * (digit - 1))
        i += 1
print(''.join(result))