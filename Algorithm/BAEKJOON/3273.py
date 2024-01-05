# import sys

# n = int(input())
# lst = list(map(int, sys.stdin.readline().split()))
# x = int(input())

# cnt = 0
# for i in range(n-1):
#   if (x-lst[i]) in lst[i+1::]:
#     cnt += 1

# print(cnt)


import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
X = int(input())
lst.sort()
left, right = 0, n - 1
ans = 0
while left < right:
    tmp = lst[left] + lst[right]
    if tmp == X: ans += 1
    if tmp < X:
        left += 1
        continue
    right -= 1
print(ans)