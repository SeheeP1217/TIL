def dfs(index):
    global mn
    if index == N//2:
        start_sm = 0
        link_sm = 0
        for i in range(N):
            if i not in start:
                link.append(i)
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                start_sm += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                link_sm += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        gap = abs(start_sm-link_sm)
        if gap < mn:
            mn = gap
        link.clear()
        return
    for i in range(N):
        if i in start:
            continue
        if len(start)>0 and start[len(start)-1]>i:
            continue
        start.append(i)
        dfs(index + 1)
        start.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = []
link = []

mn = 1e9
dfs(0)
print(mn)

