from collections import deque
def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    tmp = []

    q.append(s)
    visited[s] = 1
    while q:
        i = q.popleft()
        # for

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+2)] + [[0]+ list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
    lst = []


    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt = 1
            if arr[i][j] + 1 == arr[i+1][j] or arr[i][j] + 1 == arr[i-1][j] or arr[i][j] + 1 == arr[i][j-1] or arr[i][j] + 1 == arr[i][j+1]:
                cnt += 1
                lst.append(arr[i][j])
    print(lst)

