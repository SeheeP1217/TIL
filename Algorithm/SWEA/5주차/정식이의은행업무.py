import copy

def change(num, N, lst):
    global lst_N
    for i in range(N):
        lst = copy.deepcopy(num)
        for j in range(N):
            if lst[i] != j:
                lst[i] = j
            sm = 0
            for k in range(N):
                sm += int(lst[k]) * (N ** (len(lst)-k-1))
                lst_N.append(sm)



T = int(input())
for tc in range(1, T+1):
    nm_2 = list(input())
    nm_3 = list(input())

    lst_2 = copy.deepcopy(nm_2)
    lst_3 = copy.deepcopy(nm_3)

    lst_N = []
    change(nm_2, 2)
    print(lst_N)