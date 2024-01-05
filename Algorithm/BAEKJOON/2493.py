import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

ans = [0]
stack = [[0, lst[0]]]
for i in range(1, N):
    while stack:
        if stack[-1][1] > lst[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, lst[i]])



print(*ans)