from collections import deque
import queue

INF = 1e9

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

#최단거리 계산
def bfs():
    dist = [[-1]*n for _ in range(n)]
    queue = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] <= now_size and dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y]+1
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= arr[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        arr[now_x][now_y] = 0
        ate += 1
    if ate >= now_size:
        now_size += 1
        ate = 0
