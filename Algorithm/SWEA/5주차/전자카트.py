def f(cnt, now, sm):
    global ans
    if ans < sm:
        return
    if cnt == N:
        sm += arr[now][0]
        if ans > sm:
            ans = sm
        return
    for next in range(1, N):
        if now != next and not visited[next]:
            visited[next] = 1
            f(cnt + 1, next, sm + arr[now][next])
            visited[next] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = N * N * 100
    f(1, 0, 0)
    print(f"#{tc} {ans}")