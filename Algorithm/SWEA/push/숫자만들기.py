def perm(arr, n):
    operator = []
    if n > len(arr):
        return operator
    if n == 1:
        for i in arr:
            operator.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                operator.append([arr[i]] + p)
    return operator


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, mul, divi = map(int, input().split())
    num = list(map(int, input().split()))

    oper = []
    for i in range(plus):
        oper.append('a')
    for i in range(minus):
        oper.append('b')
    for i in range(mul):
        oper.append('c')
    for i in range(divi):
        oper.append('d')

    case = perm(oper, len(oper))
    lst = []
    for m in range(len(case)):
        cal = int(num[0])
        for n in range(N-1):
            if case[m][n] == 'a':
                cal += int(num[n+1])
            elif case[m][n] == 'b':
                cal -= int(num[n+1])
            elif case[m][n] == 'c':
                cal *= int(num[n+1])
            elif case[m][n] == 'd':
                if cal < 0:
                    cal //= int(num[n+1])
                    cal += 1
                else:
                    cal //= int(num[n+1])

        lst.append(cal)
    print(max(lst))
    print(min(lst))