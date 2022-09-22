def dfs(ci, cj, sm):
    global ans
    if ans <= sm:
        return
    if ci == N-1 and cj == N-1:
        if ans > sm:
            ans = sm
        return
    if ci < N-1:
        dfs(ci+1, cj, sm + arr[ci+1][cj])
    if cj < N-1:
        dfs(ci, cj+1, sm + arr[ci][cj+1])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10*N*2
    dfs(0, 0, arr[0][0])
    print(f"#{tc} {ans}")


