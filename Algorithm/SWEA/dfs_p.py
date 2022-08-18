def DFS(start):
    # [1] stk 등 필요자료구조 초기화
    stk = []
    visited = [0] * (V + 1)

    # [2] DFS 시작작업
    s = start
    visited[s] = 1
    sols.append(s)

    while True:
        for e in range(1, V + 1):
            # s와 연결된, 안 가본곳이면
            if visited[e] == 0 and adj[s][e] == 1:
                stk.append(s)  # 돌아올 곳을 push

                s = e
                visited[e] = 1
                sols.append(e)
                break
        else:  # 현재 s 기준으로 방문가능한 곳 없음!
            if stk:
                s = stk.pop()
            else:  # stack empty
                break


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = adj[j][i] = 1  # 양방향

    sols = []
    DFS(1)
    print(f'#{test_case}', *sols)