N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M-1):
        if arr[i][j] == 1 and arr[i][j+1] == 0:
            for dj in range(1, M - j):
                if arr[i][j+dj] == 0:
                    cnt += 1
                else:
                    break

print(cnt)
