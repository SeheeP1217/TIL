T = int(input())
for tc in range(1, T+1):
    cost_d, cost_m, cost_3m, cost_y = map(int, input().split())
    cnt = list(map(int, input().split()))

    cost = []   # 나올 수 있는 가격 종류
    visited = [0 for _ in range(12)]
    # 한달 기준 각 요금
    for i in range(len(cnt)):
        if cnt[i] > cost_m/cost_d:
            cnt[i] = cost_m
        else:
            cnt[i] = cnt[i] * cost_d
    # 세달씩 합치기
    for j in range(10):
        if cnt[j]+cnt[j+1]+cnt[j+2] > cost_3m and sum(visited[j:j+2]) == 0:
            cnt[j] = cost_3m
            cnt[j+1] = 0
            cnt[j+2] = 0
            visited[j] = 1
            visited[j+1] = 1
            visited[j+2] = 1
    ans = sum(cnt)
    # 1년요금이랑 비교하기
    if sum(cnt) > cost_y:
        ans = cost_y

    print(f"#{tc} {ans}")


