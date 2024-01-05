import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

# 중앙값
if (N % 2 == 0):
  print(lst[N//2 - 1])
else:
  print(lst[N//2])