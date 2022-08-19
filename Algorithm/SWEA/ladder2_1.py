T = int(input())
for tc in range(1, T+1):
    rows = cols = 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    st = []
    cnt = 0
    for i in range(100):
        for j in range(100):
            if i == 0 and arr[i][j] == 1:
                #st.append(j)
                #for k in st:
                i += 1
                cnt += 2
                if j < 99 and arr[i][j+1] == 1:    #오른쪽이 1이면
                    j += 1
                    cnt += 1
                elif j > 0 and arr[i][j-1] == 1:  #왼쪽
                    j -= 1
                    cnt += 1
                else:
                    i += 1
                    cnt += 1
    print(cnt)


