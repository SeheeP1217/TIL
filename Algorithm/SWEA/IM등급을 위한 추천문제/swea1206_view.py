for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, len(lst)-2):
        gb = []
        for j in range(1, 3):
            gb.append(lst[i]-lst[i-j])
            gb.append(lst[i]-lst[i+j])
        mn = lst[i]
        for k in gb:
            if k < mn:
                mn = k
        if mn > 0:
            ans += mn
    print(f"#{tc} {ans}")