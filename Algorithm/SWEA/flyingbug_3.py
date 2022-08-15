T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]  #상하
    dy = [0, 1, 0, -1]  #좌우
    dc1 = [1, 1, -1, -1] #대각선1
    dc2 = [-1, 1, 1, -1]#대각선2
    result = 0

    for i in range(N):
        for j in range(N):
            sum1 = arr[i][j]    #상하좌우
            sum2 = arr[i][j]    #대각선
            for a in range(4):
                for b in range(1, M):
                    x = i + dx[a] * b
                    y = j + dy[a] * b
                    c1 = i + dc1[a] * b
                    c2 = j + dc2[a] * b
                    if 0 <= x < N and 0 <= y < N:
                        sum1 += arr[x][y]
                    if 0 <= c1 < N and 0 <= c2 < N:
                        sum2 += arr[c1][c2]
            if result < sum1:
                result = sum1
            if result < sum2:
                result = sum2
    print(f"#{test_case} {result}")

