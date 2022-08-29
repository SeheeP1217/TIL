T = int(input())
for test_case in range(1, T+1):
    N, K1, K2 = map(int, input().split())
    lst = list(map(int, input().split()))

    possible = []
    lst.sort()

    rng = []
    for a in lst:
        if len(rng) == 0:
            rng.append(a)
        elif rng[-1] != a:
            rng.append(a)
        else:
            continue
    for i in rng:
        for j in rng:
            c1 = c2 = c3 = 0
            for k in lst:
                if k < i:
                    c1 += 1
                elif k >= j:
                    c3 += 1
                elif i <= k < j:
                    c2 += 1

            if K1 <= c1 <= K2 and K1 <= c2 <= K2 and K1 <= c3 <= K2:
                possible.append(max(c1, c2, c3)-min(c1, c2, c3))
    if len(possible) == 0:
        print(f"#{test_case} -1")
    else:
        Answer = min(possible)
        print(f"#{test_case} {Answer}")