def dfs(n):
    for j in range(1, V + 1):
        if adj[n][j] == 1 and visited[j] == 0:
            ans.append(j)
            visited[j] = 1
            dfs(j)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1

    visited = [0] * (V + 1)
    ans = []

    ans.append(1)
    visited[1] = 1
    dfs(1)

    print(f'#{test_case}', *ans)