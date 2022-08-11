T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = []
    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in m:
        cnt.append(N // i)
        N = N % i
    print(f'#{test_case}')
    print(cnt)
