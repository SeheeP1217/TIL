T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sm = 0
    for i in range(N//2+1):
        for j in range(N//2-i, N//2+i+1):
            sm += arr[i][j]

    for i in range(N//2+1,N):
        for j in range(N//2-N+i+1, N//2+N-i):
            sm += arr[i][j]
    print(f"#{tc} {sm}")


