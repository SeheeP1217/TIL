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


# def postord(n):
#     if n <= N:
#         if lst[n] == 0:  # 하위노드 계산이 필요
#             return postord(n * 2) + postord(n * 2 + 1)
#         else:
#             return lst[n]
#     return 0

# T = int(input())
# for test_case in range(1, T + 1):
#     N, M, L = map(int, input().split())
#     lst = [0] * (N + 1)
#     for _ in range(M):
#         n, v = map(int, input().split())
#         lst[n] = v
#
#     ans = postord(L)
#     print(f'#{test_case} {ans}')