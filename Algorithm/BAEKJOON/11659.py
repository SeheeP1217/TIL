N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = []
for _ in range(M):
    s, e = map(int, input().split())

    sm = 0
    for i in range(s-1, e):
        sm += lst[i]

    ans.append(sm)
for j in range(len(ans)):
    print(ans[j])
