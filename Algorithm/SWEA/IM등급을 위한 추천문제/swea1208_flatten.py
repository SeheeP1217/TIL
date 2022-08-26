for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for _ in range(N):
        for i in range(len(lst)):
            if lst[i] == max(lst):
                lst[i] -= 1
                break
        for j in range(len(lst)):
            if lst[j] == min(lst):
                lst[j] += 1
                break
    print(f"#{tc} {max(lst) - min(lst)}")