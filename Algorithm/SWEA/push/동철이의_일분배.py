def dfs(n, mer):
    global ans

    if ans >= mer:
        return

    if n == N:
        ans = max(ans, mer)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, mer*arr[n][j]/100)
            v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0]*N
    ans = 0

    dfs(0, 1)

    print(f"#{tc}", "{:.6f}".format(ans*100))