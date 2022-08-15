T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    #가로 세로 N개의 칸
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    # 0~(N-M) 순회
    for i in range(N-M+1):
        for j in range(N-M+1):
            sm = 0
            # 선택한 칸 순회
            for di in range(M):
                for dj in range(M):
                    sm += arr[i+di][j+dj]
            if sm > mx:
                mx = sm
    print(f"#{test_case} {mx}")
