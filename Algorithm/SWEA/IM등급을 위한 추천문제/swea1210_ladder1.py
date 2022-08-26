for tc in range(1, 11):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for i in range(100):
        for j in range(100):
            while i < 99:
                if arr[0][j] == 1:
                    i += 1
                if arr[i][j-1] == 1:
                    arr[i][j-1] = 2
                    j = j-1
                elif arr[i][j+1] == 1:
                    arr[i][j+1] = 2
                    j = j+1
                elif arr[i+1][j] == 1:
                    arr[i+1][j] == 2
                    i = i+1
                if arr[i][j] == 2:
                    print(i, j)
                    break
