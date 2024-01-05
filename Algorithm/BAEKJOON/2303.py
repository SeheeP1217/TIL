import sys
from itertools import combinations

N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

ans = 0
ans_max = 0

for i in range(N):
  combination_value = list(combinations(lst[i], 3))
  sm = 0
  for j in combination_value:
    sm = max(sm, sum(j) % 10)

    if sm >= ans_max:
      ans = i + 1
      ans_max = sm

print(ans)
