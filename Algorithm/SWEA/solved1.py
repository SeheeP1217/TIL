T = int(input())
for test_case in range(1, T+1):

    #1. count 배열(K칸 가고 충전소 없으면 back)은 IM 패스는 가능하겠지만 비효율인 방법
    #2. 처음에 list에 N을 append하고 시작 / 일단 충전했다치고 진행하며 K칸 안에 충전소가 2개 이상이면 마지막 충전소로 인정 및 새로운 시작점으로 갱신
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.append(N)
    i = ans =  start = last = 0
    
    while i < M+1:
        if lst[i] - start <= K:     #start~현재위치 이동가능?
            last = lst[i]
            i += 1                  #i는 더 진행이 가능
        else:
            if lst[i] - last > K:   #종점까지 못가는 경우 0 출력
                ans = 0
                break               #더이상 루프를 돌 이유가 없어서 루프 탈출
            else:
                start = last        #start 지점을 last로 바꾸고 충전횟수 +1
                ans += 1
    print(f"#{test_case} {ans}")