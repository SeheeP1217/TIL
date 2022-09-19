T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))

    for i in range(lst):
        if lst[i] == 'A':
            lst[i] = 10
        elif lst[i] == 'B':
            lst[i] = 11
        elif lst[i] == 'C':
            lst[i] = 12
        elif lst[i] == 'D':
            lst[i] = 13
        elif lst[i] == 'E':
            lst[i] = 14
        elif lst[i] == 'F':
            lst[i] = 15