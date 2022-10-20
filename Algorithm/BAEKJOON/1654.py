K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))

#이진탐색
start = 1
end = max(lst)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += lst[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)                  #최대길이이므로 end 출력
