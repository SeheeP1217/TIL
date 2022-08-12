#기존 사다리 타기와 동일하게 진행
#진행을 하며 1을 누적해서 더해간 후 가장 작은 값

T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))

    base = [[0] * 100 for _ in range(100)]

    #첫번째 줄에서 1인 값 순서대로 더하며 내려가기
    for i in range(lst.count(1)):
        one = lst[0].index(1)
        row = 0
        col = one
        cnt = 0     #사다리 동선 하나가 이동하는 거리
        cnt_lst = []    #사다리 거리 총 리스트 -> 가장 작은 것의 시작 값 구해야함
        while row != 99:
            base[row][col] = 1
            #오른쪽으로 돌기
            if col + 1 <= 99 and lst[row][col+1] and base[row][col+1] == 0:
                col += 1
                cnt += 1
                continue
            #왼쪽으로 돌기
            elif col - 1 >= 0 and lst[row][col-1] and base[row][col-1] == 0:
                col -= 1
                cnt += 1
                continue
            #양옆이 없다면 아래로
            else:
                row += 1
                cnt += 1
            cnt_lst.append(cnt)
    print(cnt)