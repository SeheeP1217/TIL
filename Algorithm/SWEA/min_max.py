T = int(input())        #테스트케이스
for i in range(T):    #테스트케이스 돌기
    N = int(input())    #자료 개수
    lst = list(map(int, input().split()))
    maxT = lst[0]  # 임의로 첫번째 값 최대로 설정
    minT = lst[0]  #임의로 첫번째 값 최소로 설정
    for j in range(N):                      #자료 돌기
        if lst[j] > maxT:                   #최댓값보다 크면 변경
            maxT = lst[j]
        if lst[j] < minT:                   #최솟값보다 작으면 변경
            minT = lst[j]
    gap = maxT - minT                   #최댓값-최솟값
    print(f"#{T} {gap}")
