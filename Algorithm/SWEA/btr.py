import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    row = N
    col = 2
    for i in range(N-1):
        if lst[i][1] > lst[i+1][0]:
            ans += 1
    #for i in range(1, N):
    #    if lst[2*i-1] > lst[2*i]:
    #        ans += 1
    print(f"#{test_case} {ans}")
