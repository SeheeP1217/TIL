T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bs = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bs[j] += 1
    arr = []
    P = int(input())
    for i in range(N):
        n = int(input())
        arr.append(bs[n])
    print(f"#{test_case}", *bs)
