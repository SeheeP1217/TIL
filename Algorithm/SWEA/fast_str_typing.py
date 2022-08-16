




T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    rst = 0
    cnt = 0
    for i in range(len(A)-len(B)+1):
        if A[cnt:cnt+len(B)] == B:
            rst += 1
            cnt = len(B) + cnt - 1
        cnt += 1
    rst = len(A) - rst*len(B) + rst
    print(f"#{tc} {rst}")
