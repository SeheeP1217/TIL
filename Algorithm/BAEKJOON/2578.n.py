rows = cols = 5
c_arr = [[0 for j in range(cols)] for i in range(rows)]
s_arr = [[0 for b in range(cols)] for a in range(rows)]
for i in range(5):
    c_lst = list(map(int, input().split()))
    k = 0
    for j in range(5):
        c_arr[i][j] = c_lst[k]
        k += 1
for a in range(5):
    s_lst = list(map(int, input().split()))
    c = 0
    for b in range(5):
        s_arr[a][b] = s_lst[c]
        c += 1

#s_lst 의 숫자를 따라 c_lst에 해당하는 위치를 0으로 바꾸기
for s in s_lst:
    for c in c_lst:
        if s == c:
            c = 0
            for i in range(5):
                for j in range(5):
                    c_arr[i][j]
