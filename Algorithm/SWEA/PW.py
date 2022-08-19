for tc in range(1, 11):
    N, pw = input().split()
    stk = []
    for i in pw:
        if stk == []:
            stk.append(i)
        elif i == stk[-1]:
            stk.pop()
        else:
            stk.append(i)
    print(f"#{tc}", ''.join(stk))
