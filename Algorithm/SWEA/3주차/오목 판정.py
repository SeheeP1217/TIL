T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'NO'
    for i in range(N):
        for j in range(N-4):
            if arr[i][j] == 'o' and arr[i][j+1] == 'o' and arr[i][j+2] == 'o' and arr[i][j+3] == 'o' and arr[i][j+4] == 'o':
                ans = 'YES'
                break
    for j in range(N):
        for i in range(N-4):
            if arr[i][j] == 'o' and arr[i+1][j] == 'o' and arr[i+2][j] == 'o' and arr[i+3][j] == 'o' and arr[i+4][j] == 'o':
                ans = 'YES'
                break
    for i in range(N-4):
        for j in range(N-4):
            if arr[i][j] == 'o' and arr[i+1][j+1] == 'o' and arr[i+2][j+2] == 'o' and arr[i+3][j+3] == 'o' and arr[i+4][j+4] == 'o':
                ans = 'YES'
                break
    for i in range(N-4):
        for j in range(4, N):
            if arr[i][j] == 'o' and arr[i+1][j-1] == 'o' and arr[i+2][j-2] == 'o' and arr[i+3][j-3] == 'o' and arr[i+4][j-4] == 'o':
                ans = 'YES'
                break
    print(f"#{tc} {ans}")