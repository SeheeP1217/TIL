for test_case in range(1, 11):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(100))
    #100*100칸
    base = [[0] * 100 for _ in range(100)]
    #마지막줄에서 2인 값 찾기
    two = arr[99].index(2)
    row = 99
    col = two
    while row != 0:
        base[row][col] = 1
        if col - 1 >= 0 and arr[row][col-1] and base[row][col-1] == 0:
            col -= 1
            continue
        elif col + 1 < 100 and arr[row][col+1] and base[row][col+1] == 0:
            col += 1
            continue
        else:
            row -= 1

    ans = col
    print(f"#{N} {ans}")
