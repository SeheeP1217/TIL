T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    ans = 0
    c_lst = []
    for i in range(N+2):
        cnt = 0
        for j in range(N+2):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                c_lst.append(cnt)
                cnt = 0
    for j in range(N+2):
        cnt = 0
        for i in range(N+2):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                c_lst.append(cnt)
                cnt = 0
    for c in c_lst:
        if c == K:
            ans += 1
    print(f"#{tc} {ans}")
