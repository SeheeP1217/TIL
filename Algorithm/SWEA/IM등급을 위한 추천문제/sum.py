for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    lst = []
    for i in range(100):
        sm = 0
        for j in range(100):
            sm += arr[i][j]
        lst.append(sm)
    for j in range(100):
        sm = 0
        for i in range(100):
            sm += arr[i][j]
        lst.append(sm)
    for i in range(100):
        sm = 0
        sm += arr[i][i]
        lst.append(sm)
    for i in range(100):
        sm = 0
        sm += arr[i][99-i]
        lst.append(sm)
    print(f"#{tc} {max(lst)}")
