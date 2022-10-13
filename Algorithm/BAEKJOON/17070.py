""" 
새 집의 크기 : N*N
r: 행의 번호
c: 열의 번호
행과 열의 번호는 1부터 시작
파이프는 (1,1), (1,2)를 차지하고 있고 (N,N)으로 이동시키는 방법
1은 벽이니 지나갈 수 없고 수직으로 이동할 수 없음 대각선으로 이동하는 경우 우, 하, 우하 모두 벽이 아니어야함
"""

"""
[DFS 풀이]
Python3 시간초과
PyPy3 852ms

import sys
input = sys.stdin.readline

def dfs(now_y, now_x, direction):
    global cnt
    if (now_y, now_x) == (N-1, N-1):
        cnt += 1
        return
    if direction == garo or direction == daegak:
        if now_x+1 < N and arr[now_y][now_x+1] == 0:
            dfs(now_y, now_x+1, garo)
    if direction == sero or direction == daegak:
        if now_y+1 < N and arr[now_y+1][now_x] == 0:
            dfs(now_y+1, now_x, sero)
    if now_y+1 < N and now_x+1 < N:
        if arr[now_y+1][now_x] == 0 and arr[now_y][now_x+1] == 0 and arr[now_y+1][now_x+1] == 0:
            dfs(now_y+1, now_x+1, daegak)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

garo = 0
sero = 1
daegak = 2

cnt = 0

dfs(0, 1, garo)
print(cnt)
"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1 # 파이프의 초기 위치

# 반복문을 통해 처음에 가로로 갈 수 있는 곳에 파이프를 이동
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

# 반복문을 통해 파이프 이동
for i in range(1, n):
    for j in range(2, n):

        # 파이프가 대각선으로 이동 가능한 경우
        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))

        # 파이프가 가로/세로로 이동 가능한 경우
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

# 3가지 방향으로 파이프가 이동해 온 경우의 합을 출력
print(sum(dp[k][-1][-1] for k in range(3)))