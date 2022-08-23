T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * (N + 2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 2:
                if arr[i+1][j] == 3 or arr[i-1][j] == 3 or arr[i][j-1] == 3 or arr[i][j+1] == 3:
                    print(f"#{tc} 1")
                    break
                elif arr[i+1][j] == 0 or arr[i-1][j] == 0 or arr[i][j-1] == 0 or arr[i][j+1] == 0:
                    if arr[i-1][j] == 0:
                        arr[i-1][j] += 2
                        i = i-1
                        continue
                    elif arr[i + 1][j] == 0:
                        arr[i + 1][j] += 2
                        i = i+1
                        continue
                    elif arr[i][j - 1] == 0:
                        arr[i][j - 1] += 2
                        j = j-1
                        continue
                    elif arr[i][j + 1] == 0:
                        arr[i][j + 1] += 2
                        j = j+1
                        continue
                else:
                    print(f"#{tc} 0")
