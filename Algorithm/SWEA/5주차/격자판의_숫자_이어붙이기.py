def f():
    if cnt == 6:
        return
    if arr[i-1][j] != '





T = int(input())
for tc in range(1, T+1):
    arr = [['o'] * 6] + [['o'] + list(input().split()) + ['o'] for _ in range(4)] + [['o'] * 6]
    lst = []
    cnt = 0
    for i in range(1, 5):
        for j in range(1, 5):
            lst.append(arr[i][j])
            f()