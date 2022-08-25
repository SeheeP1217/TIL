#N명, M초, K개
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    t = 0   #흐른 시간
    n = 0   #남아 있는 붕어빵 개수
    mxt = 0  #손님이 오는 시간 최대
    for j in lst:
        if j>mxt:
            mxt = j
    for t in range(mxt+1):
        if t > 0 and t % M == 0:
            n += K
        for i in lst:
            if t == i:
                n -= 1
                lst.remove(i)
        if n < 0:
            print(f"#{tc} Impossible")
            break
    if n >= 0:
        print(f"#{tc} Possible")
