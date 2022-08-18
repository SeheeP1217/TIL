def repeat(word):
    stack = []

    for i in word:
        if not stack:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return(len(stack))

T = int(input())
for tc in range(1, T+1):
    s = input()
    print(f"#{tc} {repeat(s)}")
