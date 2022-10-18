def dfs(x, y, cnt):
    global ans
    visited[x][y] = 1
    if [x, y] == [0, C-1]:
        if cnt == K:
            ans += 1
        return 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and arr[nx][ny] != 'T':
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0 for _ in range(C)] for _ in range(R)]
ans = 0

dfs(R-1, 0, 1)
print(ans)