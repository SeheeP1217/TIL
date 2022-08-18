T = int(input())
for t in range(1, T+1):
    txt = input()
    result = 1
    stack = []
    isIn = False
    for c in txt:
        if c == "(" or c == "{":
            stack.append(c)
            isIn = True
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
        elif c == "}":
            if stack and stack[-1] == "{":
                stack.pop()
    else:
        if stack or not isIn:
            result = 0

    print(f"#{t} {result}")