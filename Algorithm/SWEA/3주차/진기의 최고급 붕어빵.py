T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    #현재시간 t, 현재 붕어빵 개수 n
    ans = 'Possible'
    t = 0
    n = -K
    mx = 0
    for i in lst:
        if i > mx:
            mx = i
    for t in range(0, mx+1):
        if t % M == 0:
            n += K
        if t in lst:
            n -= 1
        if n < 0:
            ans = 'Impossible'
    print(f"#{tc} {ans}")
