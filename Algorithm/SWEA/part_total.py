T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    total = 0
    total_list = []
    for j in range(i,i+M):
        total += j
        total_list.append(total)
    mx = mn = total_list[0]
    for k in total_list:
        if total_list[k] > mx:
            mx = total_list[k]
        if total_list[k] < mn:
            mn = total_list[k]
    print("#{i} {mx-mn}")
