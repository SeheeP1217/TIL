T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()

    set_N = list(set(list(N)))
    lst = []
    for i in set_N:
        cnt = 0
        for j in list(M):
            if i == j:
                cnt += 1
                lst.append(cnt)
    mx = 0
    for m in lst:
        if m > mx:
            mx = m
    print(f"#{tc} {mx}")

