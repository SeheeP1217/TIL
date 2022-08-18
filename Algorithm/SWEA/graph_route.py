def DFS(start):
    stack = []
    visited = [0] * (V + 1)
    visited[start] = 1
    sols.append(start)
    while True:
        for end in range(1, V+1):
            if visited[end] == 0 and adj[start][end] == 1:
                stack.append(start)
                start = end
                visited[end] = 1
                sols.append(end)
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
    S, G = map(int, input().split())
    sols = []
    DFS(S)
    if G in sols:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

