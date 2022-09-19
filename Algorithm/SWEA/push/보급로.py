INF = 100 * 100 * 10


def bfs(si, sj):
    q = []
    s = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    s[si][sj] = 0  # 0이 아니라 arr[si][sj]인 경우도 있음

    while q:
        ci, cj = q.pop(0)  # 중복방문가능 -> q empty일 때까지 작동
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and s[ni][nj] > s[ci][cj] + 1 + max(0, arr[ni][nj] - arr[ci][cj]):
                s[ni][nj] = s[ci][cj] + max(0, arr[ci][cj])
                q.append((ni, nj))

    return s[N - 1][N - 1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0, 0)
    print(f'#{test_case} {ans}')