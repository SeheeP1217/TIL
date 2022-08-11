T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    di = [0, 1, 0, -1] #시계 방향
    dj = [1, 0, -1, 0] #우 하 좌 상
    snail = [[0]*N for _ in range(N)]
    i, j = 0, 0
    m = 0
    k = 1

    for n in range(1, N*N + 1):
        snail[i][j] = k
        k += 1
        i += di[m]
        j += dj[m]

# 범위를 벗어나거나 이미 채워져 있으면 m 방향 바꿔서 움직임
        if i < 0 or j < 0 or i >= N or j >= N or snail[i][j] != 0:
            i -= di[m]
            j -= dj[m]
            m = (m + 1) % 4
            i += di[m]
            j += dj[m]
    
    print(f"#{test_case}")
    for row in snail:
        print(*row)

    