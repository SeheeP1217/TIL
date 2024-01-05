import sys

N = input()

lst = [0] * 10

for i in range(len(N)):
  a = int(N[i])
  if a == 6 or a == 9:
    if lst[6] >= lst[9]:
      lst[9] += 1
    else:
      lst[6] += 1
  else:
    lst[a] += 1

print(max(lst))

