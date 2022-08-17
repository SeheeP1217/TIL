adjList = [[1, 2],
           [0, 3, 4],
           [0, 6],
           [1, 5],
           [1, 5],
           [3, 4, 6],
           [2, 5]]

def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    print(v)

    visited[v] = 1
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                print(v)
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top = -1
            else:
                break

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    