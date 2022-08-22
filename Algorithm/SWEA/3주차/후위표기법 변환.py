T = int(input())
for tc in range(1, T+1):
    arr = input()
    stk1 = []
    stk2 = []

    for i in arr:
        if i == '*':
            stk1.append(i)
            continue
        elif i == '+':
            stk1.append(i)
        else:
            stk2.append(i)

        if (stk1 and stk1[-1] == '*') or (len(stk1) > 1 and stk1[-1] == '+'):
            a = stk2[-2]
            b = stk2[-1]
            stk2.pop()
            stk2.pop()
            stk2.append(a + b + stk1.pop())
    print(f"#{tc}", stk2[-2]+stk2[-1]+stk1.pop())