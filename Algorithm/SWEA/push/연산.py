from collections import deque

def bfs(s):
    global cnt
    q = deque()
    q.append((s, 0))
    visited = set()
    visited.add(s)
    while q:
        num, cnt = q.popleft()
        for next_num in (num + 1, num - 1, num * 2, num - 10):
            if next_num <= int(1e6) and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))
                if next_num == M:
                    return cnt + 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    print(f"#{tc} {bfs(N)}")

