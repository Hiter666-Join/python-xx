n = int(input())
lists = []
for _ in range(n):
    num = list(map(int,input().split()))
    lists.append(num)
nums = [i for sub in lists for i in sub]
nums.sort()
for i in range(len(nums) - 1):
    a , b = nums[i],nums[i+1]
    if b == a:
        n = nums[i]
    elif b - a != 1:
        m = nums[i] + 1
print(m,n)