T = int(input())
for test_case in range(1, T + 1):
    t, N = input().split()
    lst = list(input().split())
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0]*len(num)
    ans = []
    for number in lst:
        for i in range(len(num)):
            if number == num[i]:
                cnt[i] += 1
                break
    for j in range(len(num)):
        for _ in range(cnt[j]):
            ans.append(num[j])
    print(f"#{test_case}")
    print(*ans)