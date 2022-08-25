T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    N_lst = []
    for n in range(len(lst)):
        lst[n] = [n+1, lst[n]]
    for i in range(N):
        N_lst.append(lst[0])
        lst.pop(0)
    while len(N_lst) != 1:
        if N_lst[0][1] == 1:
            if len(lst) == 0:
                N_lst.pop(0)
                continue
            else:
                N_lst.append(lst[0])
                lst.pop(0)
                N_lst.pop(0)
        else:
            N_lst.append([N_lst[0][0], N_lst[0][1] // 2])
            N_lst.pop(0)
    print(f"#{tc}", N_lst[0][0])
