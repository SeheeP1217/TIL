def partition(lst):

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_lst = partition(lst[:mid])
    right_lst = partition(lst[mid:])
    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    left_N = len(left_lst)
    right_N = len(right_lst)
    rst = [0]*(left_N+right_N)
    left_i, right_i = 0, 0
    i = 0
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    while left_i < left_N or right_i < right_N:
        if left_i < left_N and right_i < right_N:
            if left_lst[left_i] <= right_lst[right_i]:
                rst[i] = left_lst[left_i]
                i += 1
                left_i += 1
            else:
                rst[i] = right_lst[right_i]
                i += 1
                right_i += 1

        elif left_i < left_N:
            rst[i] = left_lst[left_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            rst[i] = right_lst[right_i]
            i += 1
            right_i += 1
    return rst


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    part = partition(lst)

    print(f'#{test_case} {part[N//2]} {cnt}')