T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    row = col = N
    arr = [[0 for j in range(col)] for i in range(row)]
    lst = []
    for i in range(N):
        for j in range(N):
            for m in range(M):
                left = i-m
                right = i+m
                up = j-m
                down = j+m
                if i-m < 0:
                    left = 0
                if j-m < 0:
                    up = 0
                if i+m > N:
                    right = N-1
                if j+m > N:
                    down = N-1
                sma = arr[left][j] + arr[right][j] + arr[i][up] + arr[i][down]
                smc = arr[left][up] + arr[right][up] + arr[left][down] + arr[right][down]
                lst.append(sma)
                lst.append(smc)
    mx = lst[0]
    for t in lst:
        if t > mx:
            mx = t
    print(f"#{test_case} {mx}")

