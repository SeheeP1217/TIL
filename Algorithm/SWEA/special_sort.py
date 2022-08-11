def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    bubble_sort(lst)
    ans = []
    for i in range(5):
        ans.append(lst[len(lst)-1-i])
        ans.append(lst[i])
    print(f"#{test_case} ", end="")
    print(*ans)
