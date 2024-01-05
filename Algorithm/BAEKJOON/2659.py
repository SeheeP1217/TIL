
import sys

def find_clock_num(lst):
  clock_num1 = lst[0] * 1000 + lst[1] * 100 + lst[2] * 10 + lst[3]
  clock_num2 = lst[1] * 1000 + lst[2] * 100 + lst[3] * 10 + lst[0]
  clock_num3 = lst[2] * 1000 + lst[3] * 100 + lst[0] * 10 + lst[1]
  clock_num4 = lst[3] * 1000 + lst[0] * 100 + lst[1] * 10 + lst[2]

  min_clock_num = min(clock_num1, clock_num2, clock_num3, clock_num4)

  return min_clock_num

lst = list(map(int, sys.stdin.readline().split()))

min_value = find_clock_num(lst)

cnt = 0
mn = 1111

for i in range(mn, min_value + 1):
  check_value = list(map(int, str(i)))
  if 0 not in check_value:
    if find_clock_num(check_value)==i:
      cnt += 1
print(cnt)