def dfs(idx, cnt):
    visited[idx] = 1
    for i in tree[idx]:
        if visited[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    tree = [[] for _ in range(N+1)]
    visited = [0]*(N+1)

    for _ in range(M):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s)
    
    result = dfs(1, 0)
    print(result)

