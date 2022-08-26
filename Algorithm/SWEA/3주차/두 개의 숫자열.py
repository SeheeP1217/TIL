T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    gb = len(A) - len(B)
    sm_lst = []
    if gb < 0:
        for g in range(-gb+1):
            sm = 0
            for i in range(len(A)):
                sm += A[i] * B[i+g]
            sm_lst.append(sm)
    if gb > 0:
        for g in range(gb):
            sm = 0
            for i in range(len(B)):
                sm += B[i] * A[i+g]
            sm_lst.append(sm)
    mx = 0
    for a in sm_lst:
        if a > mx:
            mx = a
    print(f"#{tc} {mx}")

