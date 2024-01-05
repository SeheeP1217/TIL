def d(n):
  char = list(str(n))
  return sum(map(int, char)) + n

d_n = []
n = 1

while d(n) <= 10045:
  d_n.append(d(n))
  n += 1

r = list(sorted(set(i for i in range(1, 10001)) - set(d_n)))


for i in range(len(r)):
  print(r[i])