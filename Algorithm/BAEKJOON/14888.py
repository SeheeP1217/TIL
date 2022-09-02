N = int(input())
lst_n = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
lst_c = []
max = -1e9
min = 1e9

for _ in range(a):
    lst_c.append('+')
for _ in range(b):
    lst_c.append('-')
for _ in range(c):
    lst_c.append('*')
for _ in range(d):
    lst_c.append('/')
print(lst_c)

