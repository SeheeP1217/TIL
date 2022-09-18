def check(si, sj):
    # [1] 위쪽체크
    for i in range(si):
        if arr[i][sj]:  # 해당좌표에 Q있다면 0
            return 0
    # [2] 좌측위쪽 대각선
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if arr[i][j]:
            return 0
        i, j = i - 1, j - 1
    # [3] 우측위쪽 대각선
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if arr[i][j]:
            return 0
        i, j = i - 1, j + 1
    return 1


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if check(n, j):
            arr[n][j] = 1
            dfs(n + 1)
            arr[n][j] = 0


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    ans = 0

    dfs(0)
    print(f'#{test_case} {ans}')