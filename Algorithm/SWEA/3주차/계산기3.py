for tc in range(1, 11):
    N = int(input())
    s = input()
    tokens = []
    stack = []
    result = []

    for i in range(N):
        if s[i].isdigit():
            tokens.append(int(s[i]))
        else:
            if s[i] == ')':
                chk = ''
                while chk != '(':
                    chk = stack.pop()
                    tokens.append(chk)
                tokens.pop()
                continue
            elif s[i] == '*':
                while stack and stack[-1] == '*' and stack[-1] != "(":
                    tokens.append(stack.pop())
            elif s[i] == '+':
                while stack and stack[-1] != "(":
                    tokens.append(stack.pop())
            stack.append(s[i])

    while stack:
        tokens.append(stack.pop())


    for i in tokens:
        if i in range(0, 10):
            result.append(i)
        else:
            if i == "+":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 + p1)
            elif i == "*":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 * p1)

    print(f'#{tc} {result[-1]}')