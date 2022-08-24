T = int(input())
for tc in range(1, T+1):
    code = list(map(int, input().split()))
    flag = 0    # 반복문 탈출을 위한 변수 초기화

    while code:
        # i를 숫자에서 빼주기 위해서 1~5까지 반복하도록 설정
        for i in range(1, 6):
            n = code.pop(0)     # code의 첫번째 값을 pop
            if n - i <= 0:      # 해당 값에서 i를 뺀 값이 0이거나 0보다 작으면
                code.append(0)  # 0을 append 하고
                flag = 1        # 반복문에서 탈출하도록 설정
                break
            else:
                code.append(n - i)  # 그 외의 경우 n-i를 append
        if flag:
            break

    print(f'#{tc}', *code)