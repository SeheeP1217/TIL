for tc in range(1, 11):
    N = int(input())
    lst = list(input())

    stk = []
    ans = 1
    while len(lst) != 0:
        if lst[0] in '([{<':
            stk.append(lst[0])
            lst.pop(0)
        elif lst[0] in ')]}>' and len(stk) == 0:
            ans = 0
            break
        elif lst[0] ==')':
            if '(' == stk[-1]:
                stk.pop(-1)
                lst.pop(0)
            else:
                ans = 0
                break
        elif lst[0] ==']':
            if '[' == stk[-1]:
                stk.pop(-1)
                lst.pop(0)
            else:
                ans = 0
                break
        elif lst[0] =='}':
            if '{' == stk[-1]:
                stk.pop(-1)
                lst.pop(0)
            else:
                ans = 0
                break
        elif lst[0] =='>':
            if '<' == stk[-1]:
                stk.pop(-1)
                lst.pop(0)
            else:
                ans = 0
                break
    if len(stk) != 0 or len(lst) != 0:
        ans = 0
        print(f"#{tc} {ans}")
        continue
    print(f"#{tc} {ans}")



