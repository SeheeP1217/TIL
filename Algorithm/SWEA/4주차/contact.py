from collections import deque
def contact(S):
    q = deque()
    visited = [0] * (N+1)
    tmp = []

    q.append(S)
    visited[S] = 1
    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = visited[i] + 1
    for idx in range(N+1):
        if visited[idx] == max(visited):
            tmp.append(idx)
    return max(tmp)

for tc in range(1, 11):
    N, S = map(int, input().split())
    adjLst = [[] for _ in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(0, N, 2):
        adjLst[lst[i]].append(lst[i+1])

    ans = contact(S)
    print(f'#{tc} {ans}')