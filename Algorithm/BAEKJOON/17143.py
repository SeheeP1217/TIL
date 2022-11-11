R, C, M = map(int, input().split())     # R, C는 격자판의 크기, M은 상어의 수

# 낚시왕이 잡은 물고기의 크기 합
fish_sum = 0
# 격자판
board = [[0]*C for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    # r, c는 상어의 위치
    # s는 속력
    # d는 이동 방향
    # z는 크기 (큰 상어가 잡아먹는다)




