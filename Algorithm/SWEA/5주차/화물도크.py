def f(i, sm):
    global ans
    if ans > sm:
        return
    if i == N:
        if ans < sm:
            ans = sm
            return

    s = lst[i][0]
    e = lst[i][1]
    if sum(hour[s:e]) == 0:
        for u in range(s, e):
            hour[u] = 1
        f(i + 1, sm + 1)
    f(i+1, sm)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    hour = [0 for _ in range(24)]
    ans = 0
    f(0, 0)
    print(f"#{tc} {ans}")


