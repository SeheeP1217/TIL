T = int(input())
for test_case in range(1, T+1):

    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.append(N)
    prev = ans =  start = 0

    #3. for문만 가지고 한번에 돌리는 방법(그리디)
    for nxt in lst:
        if nxt - prev > K: #끝까지 가지 못하는 경우
            ans = 0
            break
        if nxt - start <= K: #가능한 경우
            prev = nxt
        else:
            start = prev
            ans += 1
            prev = nxt

        #line14~19를 아래와 같이 변경도 가능

        #if nxt-start > K:
        #    start = prev
        #    ans += 1
        #prev = nxt


    print(f"#{test_case} {ans}")