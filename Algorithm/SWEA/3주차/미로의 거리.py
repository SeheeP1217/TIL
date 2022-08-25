def bfs(si, sj, ei, ej):
    visited = [[0] * N for _ in range(N)]
    q = []
    visited[si][sj] = 1
    q.append((si, sj, 0))
    while q:
        ci, cj, d = q.pop(0)
        if ci == ei and cj == ej:
            return d - 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != '1':
                visited[ni][nj] = 1
                q.append((ni, nj, d + 1))
    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)

    print(f'#{test_case} {ans}')