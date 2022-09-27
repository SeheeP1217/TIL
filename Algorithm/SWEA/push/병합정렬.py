#퀵 정렬을 구현해 N개의 정수를 리스트 A에 넣고 A[N//2]에 저장된 값을 출력

def partition(lst):
    global cnt

    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left_lst = partition(lst[:mid])
    right_lst = partition(lst[mid:])
    left_N = len(left_lst)
    right_N = len(right_lst)
    rst = [0]*(left_N + right_N)
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
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    part = partition(A)
    print(f"#{tc} {part[N//2]}")