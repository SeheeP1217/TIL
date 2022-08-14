#import sys
#sys.stdin = open("sample_input.txt", "r")

#지나가는 루트 모두에 1을 더하고 그 중 최댓값이 모두 방으로 돌아가는 최소 시간
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    #방
    arr = [list(map(int, input().split())) for _ in range(N)]
    #지나간 사람 수
    person = [0] * 200

    #왼->오 방향으로 통일
    for a in arr:
        if a[1] < a[0]:
            s, e = a[1], a[0]
        else:
            s, e = a[0], a[1]
        for i in range((s-1)//2, (e-1)//2+1):
            person[i] += 1
    ans = 0
    for p in person:
        if p > ans:
            ans = p
    print(f"#{test_case} {ans}")











#왼->오른쪽만 가능
#T = int(input())
#for test_case in range(1, T+1):
#    N = int(input())
#    lst = [list(map(int, input().split())) for _ in range(N)]
#    ans = 1
#    row = N
#    col = 2
#    for i in range(N-1):
#        if lst[i][1] > lst[i+1][0]:
#            ans += 1
    #for i in range(1, N):
    #    if lst[2*i-1] > lst[2*i]:
    #        ans += 1
#    print(f"#{test_case} {ans}")
