T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0]*(N+1)
    last = 0
    for n in lst:
        last += 1
        heap[last] = n

        c = last
        while c//2 and heap[c]<heap[c//2]:
            heap[c], heap[c//2] = heap[c//2], heap[c]
            c//= 2

    ans = 0
    c = last//2
    while c:
        ans += heap[c]
        c //= 2
    print(f'#{tc} {ans}')

