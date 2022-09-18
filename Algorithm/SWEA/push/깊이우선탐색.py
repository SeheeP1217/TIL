def dfs(c):
    for a in adjL[c]:  # c의 이웃 중
        if visited[a] == 0:  # 방문 아직 안한 친구이면
            visited[a] = 1
            dfs(a)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adjL[s].append(e)
        adjL[e].append(s)

    visited = [0] * (E + 1)
    visited[k] = 1
    dfs(1)

    print(f"#{tc}", )



