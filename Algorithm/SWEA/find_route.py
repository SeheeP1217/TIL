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

for tc in range(1, 11):
    V = 100
    T, E = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        start, end = lst[2*i], lst[2*i + 1]
        adj[start][end] = 1
    sols = []
    DFS(0)
    if 99 in sols:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
