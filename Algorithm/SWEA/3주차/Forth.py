T = int(input())
for tc in range(1, T+1):
    lst = input().split()
    stack = []
    cnt = 0
    for i in lst:
        if i.isdigit():
            stack.append(i)
            cnt += 1
        elif i == '+':
            if len(stack)<2:
                print(f"#{tc} error")
                break
            else:
                rst = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(rst)
        elif i == '-':
            if len(stack)<2:
                print(f"#{tc} error")
                break
            else:
                rst = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(rst)
        elif i == '*':
            if len(stack)<2:
                print(f"#{tc} error")
                break
            else:
                rst = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(rst)
        elif i == '/':
            if len(stack)<2:
                print(f"#{tc} error")
                break
            else:
                rst = int(stack[-2]) // int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(rst)
        elif i == '.':
            if len(stack) == 1:
                print(f"#{tc}", *stack)
            else:
                print(f"#{tc} error")
    #if lst[-1] != '.':
    #    print(f"#{tc} error")



