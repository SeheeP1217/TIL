T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    L = 10
    arr = [[0]*(L) for _ in range(L)]
    ans = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
    for i in range(L):
        for j in range(L):
            if arr[i][j] == 3:
                ans += 1
    print(f'#{test_case} {ans}')