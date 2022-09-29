T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    # 최대공약수
    for i in range(A):
        if A % (A-i) == 0 and B % (A-i) == 0:
            print(A*B // (A - i))
            break
