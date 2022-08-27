for tc in range(1, 11):
    N = int(input())
    arr1 = [list(input()) for _ in range(8)]
    arr2 = list(map(list,zip(*arr1)))

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr1[i][j:j+N] == arr1[i][j:j+N][::-1]:
                cnt += 1
            if arr2[i][j:j+N] == arr2[i][j:j+N][::-1]:
                cnt += 1
    print(f"#{tc} {cnt}")