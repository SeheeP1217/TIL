INF = 50 * 10
def dijkstra(s):
    D = adj[s][::]
    v = [0] * (N+1)
    v[s] = 1

    for _ in range(N):
        mn, min_i = INF, 0
        for i in range(N+1):
            if v[i] == 0 and mn > D[i]:
                min_i, mn = i, D[i]
        v[min_i] = 1
        for i in range(N+1):
            D[i] = min(D[i], D[min_i] + adj[min_i][i])
    return D[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    for i in range(N):
        adj[i][i] = 0

    ans = dijkstra(0)
    print(f'#{tc} {ans}')