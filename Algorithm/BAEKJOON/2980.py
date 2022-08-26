def func(num):
    if num == 1:
        if lst[0][0] % (lst[0][1] + lst[0][2]) >= lst[0][1]:
            return lst[0][0]
        else:
            return lst[0][0] + lst[0][1] - (lst[0][0] % (lst[0][1] + lst[0][2]))
    if (func(num-1) + lst[num-1][0] - lst[num-2][0]) % (lst[num-1][1] + lst[num-1][2]) >= lst[num-1][1]:
        return func(num-1) + lst[num-1][0] - lst[num-2][0]
    else:
        return func(num-1) + lst[num-1][0] - lst[num-2][0] + lst[num-1][1] - ((func(num-1) + lst[num-1][0] - lst[num-2][0]) % (lst[num-1][1] + lst[num-1][2]))


N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

#t는 현재시간, m은 현재위치
#점화식 f(x) = f(x-1) + D(x) - D(x-1) + 신호등

print(func(N)+5)

