#매번 최대, 최소 찾아서 한칸씩 빼고 더하기

for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int,input().split()))

    # max,min 값 구하기
    for i in range(N):     #N번 반복
        mx = mn = lst[0]
        for j in lst:
            if j > mx:
                mx = j
            if j < mn:
                mn = j      

        # lst에서 max는 -1, min은 +1 한번씩만 해주기(공통 숫자 피하기)
        for m in range(len(lst)):
            if lst[m] == mx:
                lst[m] -= 1
                break
        for m in range(len(lst)):
            if lst[m] == mn:
                lst[m] += 1
                break

        # 다시 max, min 값
        mx = mn = lst[0]
        for j in lst:
            if j > mx:
                mx = j
            if j < mn:
                mn = j

        # flat이면 종료
        if mx - mn <= 1:
            break

    print(f"#{test_case} {mx-mn}")