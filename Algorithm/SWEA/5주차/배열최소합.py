def min_sum(n, ssum):
    global sm
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            ssum += arr[n][i]
            if ssum < sm:
                if n == N - 1:
                    sm = ssum
                else:
                    min_sum(n + 1, ssum)
            visited[i] = 0
            ssum -= arr[n][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    sm = 10 * N
    min_sum(0, 0)
    print(f'#{tc} {sm}')

