def preorder(n):
    if n:
        lst.append(n)
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E = int(input())
    arr = list(map(int, input().split()))
    V = E + 1
    root = 1
    lst = []

    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(E-1):
        p, c = arr[(i)*2], arr[(i)*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    preorder(root)
    print(f"#{tc}", *lst)