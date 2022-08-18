T = int(input())
for tc in range(1, T+1):
    N = input()
    stack = []
    ans = 0
    for i in N:
        if i in '{(':
            stack.append(i)
        elif i in ')}':
            if len(stack) == 0:
                break
            if stack and (stack[-1] == '{' and i == '}') or (stack[-1] == '(' and i == ')'):
                stack.pop()
            else:
                break
    else:
        if not stack:
            ans = 1
    print(f"#{tc} {ans}")