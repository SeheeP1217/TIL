N = int(input())
M = int(input())

lst = [0] * (N+1)
for i in range(M):
  seat = int(input())
  lst[seat] = -1

print(lst)