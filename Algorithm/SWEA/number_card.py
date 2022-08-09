T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input()))
    cnt = [0]*10
    total = 0

    for i in range(N):
        cnt[int(lst[i])] += 1
    for j in range(len(cnt)):
        if cnt[j] >= total:
            total = cnt[j]
            num = j
    print(f"#{test_case} {num} {total}")
    