def node_number():
    sm = 0
    for i in range(M):
        for j in range(10):
            if arr[i][0] >= L * (2 ** j) and arr[i][0] < (L+1) * (2 ** j):
                sm += arr[i][1]
    print(sm)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    print(f"#{tc}", end=' ')
    node_number()