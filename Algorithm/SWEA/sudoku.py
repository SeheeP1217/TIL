T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if arr[i][j] in lst:
                a = arr[j]
                lst.pop
        if lst != []:
            ans = 0
            break
    for j in range(9):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if arr[i][j] in lst:
                a = arr[i]
                lst.pop(a)
        if lst != []:
            ans = 0
            break
    print(ans)


            