def bfs(v):
    q = []
    visited = [0]*(V+1)
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for e in range(E):
            if node[e][0] == v and visited[node[e][1]] == 0:
                q.append(node[e][1])
                visited[node[e][1]] = 1
                distance[node[e][1]] = distance[v] + 1
            if node[e][1] == v and visited[node[e][0]] == 0:
                q.append(node[e][0])
                visited[node[e][0]] = 1
                distance[node[e][0]] = distance[v] + 1
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    distance = [0]*(V+1)
    bfs(S)
    print(f"#{tc} {distance[G]}")