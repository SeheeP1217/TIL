def postorder(n):
    global stack
    if tree[n]:
        postorder(ch1[n])
        postorder(ch2[n])
        if type(tree[n]) == int:
            stack += [tree[n]]
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[n] == '+':
                stack += [b+a]
            elif tree[n] == '-':
                stack += [b-a]
            elif tree[n] == '/':
                stack += [b/a]
            elif tree[n] == '*':
                stack += [b*a]

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for _ in range(N):
        arr = input().split()
        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        else:
            tree[int(arr[0])] = int(arr[1])
    stack = []
    postorder(1)
    print(f"#{tc} {int(stack[0])}")