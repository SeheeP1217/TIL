T = 1

for test_case in range(1, T + 1) :
    N = int(input())
    lst = list(map(int,input().split()))
    rv = 0
    for i in range(2, N-2) :
        if lst[i]-lst[i-1] > 0 and lst[i]-lst[i-2] > 0 and lst[i]-lst[i+1] > 0 and lst[i]-lst[i+2] > 0:
            minC = lst[i]-lst[i-2]
            if lst[i]-lst[i-1] < minC:
                minC = lst[i]-lst[i-1]
            if lst[i]-lst[i+1] < minC:
                minC = lst[i]-lst[i+1]
            if lst[i]-lst[i+2] < minC:
                minC = lst[i]-lst[i+2]
            rv += minC
print(f"#{test_case} {rv}")
