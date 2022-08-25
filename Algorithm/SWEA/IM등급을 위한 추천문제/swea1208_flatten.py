for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    sm = 0
    for i in lst:
        sm += i
    avg = sm // len(lst)
