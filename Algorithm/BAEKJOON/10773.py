from collections import deque

N = int(input())
lst = deque()
for _ in range(N):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)

if len(lst) == 0:
    print(0)
else:
    print(sum(lst))