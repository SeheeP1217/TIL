def quick(lst):
    if len(lst) < 2 :
        return lst
    mid = lst[len(lst)//2]
    left_lst, mid_lst, right_lst = [], [], []
    for i in lst:
        if i < mid:
            left_lst.append(i)
        elif i > mid:
            right_lst.append(i)
        else:
            mid_lst.append(i)
    return quick(left_lst)+mid_lst+quick(right_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    part = quick(A)

    print(f"#{tc} {part[N//2]}")