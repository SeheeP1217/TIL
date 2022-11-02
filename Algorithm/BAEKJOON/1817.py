N, M = map(int, input().split())
lst = list(map(int, input().split()))

box = 0
sm = 0
for i in range(len(lst)):
    if i == len(lst)-1 and sm < M:
        box += 1
        break

    if sm + lst[i] > M:
        box += 1
        sm = lst[i]
    elif sm + lst[i] == M:
        box += 1
        sm = 0
    else:
        sm += lst[i]
print(box)