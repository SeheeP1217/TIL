T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    x, y, d, K = [], [], [], []
    for i in range(N):
        x.append(lst[i][0])
        y.append(lst[i][1])
        d.append(lst[i][2])
        K.append(lst[i][3])

    # 세로에서 충돌(x가 같은 경우)
    # 가로에서 충돌(y가 같은 경우)
    lst_v = []
    lst_h = []
    for a in range(N-1):
        for b in range(a+1, N):
            if x[a] == x[b]:
                if y[a] < y[b] and d[a] == 0 and d[b] == 1:
                    lst_v.append([a, b])
                elif y[a] > y[b] and d[a] == 1 and d[b] == 0:
                    lst_v.append([a, b])
            if y[a] == y[b]:
                if x[a] < x[b] and d[a] == 3 and d[b] == 2:
                    lst_h.append([a, b])
                elif x[a] > x[b] and d[a] == 2 and d[b] == 3:
                    lst_h.append([a, b])
    print(lst_v)
    print(lst_h)


