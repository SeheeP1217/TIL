def dfs(n, cnt):
    global ans
    if cnt >= ans:
        return
    if n >= (N-1):
        ans = min(cnt, ans)
        return
    for i in range(1,lst[n]+1):
        dfs(n+i, cnt+1)

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    ans = 10000
    dfs(0, -1)
    print(f'#{test_case} {ans}')