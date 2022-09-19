T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    num_10 = []

    for i in range(len(lst)//7):
        nm = 0
        num_2 = lst[7*i:7*i+7]
        for j in range(7):
            nm += num_2.pop(0) * 2**(6-j)
        num_10.append(nm)
    print(f'#{tc}', *num_10)