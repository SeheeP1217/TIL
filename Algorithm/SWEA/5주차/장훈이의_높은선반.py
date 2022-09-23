T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []
    ans = 0

    n = len(arr)
    for i in range(1<<n):
        li = []
        for j in range(n):
            if i & (1 << j):
                li.append(arr[j])

        sm = 0
        for p in range(len(li)):
            sm += li[p]

            if sm >= B:
                lst.append(sm)

    lst.sort()
    ans = min(lst) - B

    print(f"#{tc} {ans}")
