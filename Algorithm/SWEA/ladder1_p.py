import sys
sys.stdin = open("input.txt", "r")

T = 3
for test_case in range(1, T+1):
    _ = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    #초기값 설정
    i, j = N-1, 0

    #목적지(출발지) arr[][] == 2
    for tj in range(N):
        if arr[i][tj] == 2:
            j = tj
            break

    while i > 0:
        if j > 0 and arr[i][j-1]==1:  #왼쪽에 이동가능한 길이 있음
            arr[i][j] = 0
        elif j <99 and arr[i][j+1]==1: #오른쪽방향 이동가능 체크
            arr[i][j] = 0
        else:
            i = -1

    print(f'#{test_case} {j}')
