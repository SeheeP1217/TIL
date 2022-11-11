N = int(input())

ans = 0
for _ in range(N):
    lst = list(input())
    check_list = ['C']
    for i in range(len(lst)):
        if lst[i]==check_list[-1]:
            check_list.pop(-1)
        else:
            check_list.append(lst[i])
    if len(check_list) == 1:
        ans += 1
print(ans)
    
    
