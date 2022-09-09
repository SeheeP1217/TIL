from collections import deque

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for i in range(n)] for depth in range(h)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i, j, k])
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                queue.append([nz, nx, ny])

flag = False
for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                flag = True
                break

if flag:
    print(-1)
else:
    max_value = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                max_value = max(max_value, arr[i][j][k])
    print(max_value - 1)