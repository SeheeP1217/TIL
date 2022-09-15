def subtree(N):
    lst.append(N)
    while len(root) != 0:
        if root[0] not in lst:
            root.pop(0)
            root.pop(0)
        else:
            lst.append(root[1])
            root.pop(0)
            root.pop(0)
    print(len(lst))

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    root = list(map(int, input().split()))
    lst = []
    print(f'#{tc}', end=' ')
    subtree(N)