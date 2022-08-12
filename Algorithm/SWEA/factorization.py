T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    for i in range(5):
        while N % num[i] == 0:
            cnt[i] += 1
            N = N // num[i]
    print("#{} {}".format(test_case, ' '.join(map(str,cnt))))
