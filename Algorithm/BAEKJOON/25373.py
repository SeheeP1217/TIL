N = int(input())
condition = sum(range(1, 8)) # 7일 모두 시청해야 하는 경우의 최소 영상 개수 (기준점)
avg, remain = divmod(N, 7)
result = 0

# 모두 시청하는데 7일이 필요하지 않는 경우
if N < condition:
    num = 0
    num_sum = 0
    while num_sum < condition: 
        num += 1
        num_sum += num
    result = num

# 7일 모두 시청해야 하는 경우
else:
    if remain:
        result += 1
    result += (avg + 3)

print(result)