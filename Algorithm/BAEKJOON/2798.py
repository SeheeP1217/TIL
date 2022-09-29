from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
result = result + list(combinations(lst, 3))
sm_lst = []
for i in result:
    sm = 0
    for j in i:
        sm += j
    sm_lst.append(sm)

sm_lst.sort(reverse=True)

for s in sm_lst:
    if s <= M:
        print(s)
        break
