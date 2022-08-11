T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    subsets = [[]]

    for i in lst:
        s = len(subsets)
        for j in range(s):
            subsets.append(subsets[j]+[i])       

    total = 0
    test = 0
    for a in subsets:
        if a == []:
            continue
        for b in a:
            total += b
        if total == 0:
            test = 1
            break
        total = 0
    if test == 1:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
    
