T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = len(A)
    b = len(B)
    if a < b:
        lst = []
        c = b - a
        for i in range(c+1):
            sm = 0
            for j in range(a):
                sm += A[j] * B[i+j]
            lst.append(sm)
        mx = 0
        for m in lst:
            if m > mx:
                mx = m
        print(f"#{tc} {mx}")

    else:
        lst = []
        c = a - b
        for i in range(c+1):
            sm = 0
            for j in range(b):
                sm += A[i+j] * B[j]
            lst.append(sm)
        mx = 0
        for m in lst:
            if m > mx:
                mx = m
        print(f"#{tc} {mx}")