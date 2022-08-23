T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        sm = 0
        for di in range(N):
            j = i + di
            if j >= N:
                j = j - N
            sm += arr[j][di]
        lst.append(sm)
    #for i in range(N):
        sm = 0
        for di in range(N):
            j = i + di
            if j >= N:
                j = j - N
            sm += arr[j][N - di -1]
        lst.append(sm)
        mn = lst[0]
        for n in lst:
            if n < mn:
                mn = n
    print(f"#{tc} {mn}")

