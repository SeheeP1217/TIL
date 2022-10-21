import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleeping = list(map(int, input().split()))
start_num = list(map(int, input().split()))

num = []
for i in range(3, N+3):
    num.append(i)

for j in start_num:    
    if j in sleeping:                       # j가 졸고 있다면 break
            break                         
    for k in range(1, (N+3)//j+1):              # j의 배수
        if j*k not in sleeping and j*k in num:    # j의 배수가 졸고있지 않고, 출석안했다면
            num.remove(j*k)                         # 리스트에서 제외

for _ in range(M):
    s, e = map(int, input().split())

    cnt = 0
    for l in range(s, e+1):
        if l in num:
            cnt += 1
    print(cnt)
"""
10명의 학생 (3~12번)
1며이 졸고 있고
3명한테 보냄
7번이 졸고 있음
3, 5, 7번이 출석코드 받음
3번~12번

=> 3, 6, 9, 12, 5, 10, 

5 1 1 1
3
3
3 7

5
"""