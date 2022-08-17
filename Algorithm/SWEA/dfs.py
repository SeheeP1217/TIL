def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    visited[v] = 1
    ans = [v]
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                ans.append(v)
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top = -1
            else:
                break
    return ans

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)

    visited = [0] * N
    stack = [0] * N
    a = dfs(1, N)
    print(f"#{tc} ", end="")
    for i in a:
        print(i, end=" ")
    print()
