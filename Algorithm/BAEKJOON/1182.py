N, S = map(int, input())
lst = list(map(int, input().split()))

def recursion(count, targetNum, currentCount=0, result=0, temp_sum=0, is_index=0):
    if currentCount >= count:
        return result
    for k in range(is_index, 12):
        t_s