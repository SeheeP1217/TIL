T = int(input())
for test_case in range(1, T+1):
    rows = cols = 100
    arr = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(100):
        lst = list(map(int,input().split()))
        k = 0
        for j in range(100):
            arr[i][j] = lst[k]
            k += 1

    max1 = 0
    for i in range(100):
        sum1 = 0
        for j in arr[i]:
            sum1 += j
        if sum1 > max1:
            max1 = sum1
    for i in range(100):
        sum2 = 0
        for j in range(100):
            sum2 += arr[j][i]    
        if sum2 > max1:
            max1 = sum2
    sum3 = 0
    for i in range(100):
        sum3 += arr[i][i]
    if sum3 > max1:
        max1 = sum3

    sum4 = 0
    for i in range(100):
        sum4 += arr[i][99-i]
    if sum4 > max1:
        max1 = sum4

    print(f"#{test_case} {max1}")