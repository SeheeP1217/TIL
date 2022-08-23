def rsp(lst):
    if (lst[i]+1) % 3 == lst[i+1] % 3:
        lst.pop(lst[i])
        return lst[i+1]
    elif lst[i] % 3 == (lst[i+1] + 1) % 3:
        lst.pop(lst[i+1])
        return lst[i]
    elif lst[i] == lst[i+1]:
        lst.pop(lst[i+1])
        return lst[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N//2+1):
        print(rsp(lst[i], lst[i+1]))