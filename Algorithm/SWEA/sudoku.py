T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        for j in range(9):
            