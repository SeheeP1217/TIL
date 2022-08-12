#버블정렬
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for test_case in range(1, T+1):
    N, C = map(int, input().split())
    st = list(map(int, input().split()))
    lst = bubble_sort(st)
    total = 0
    i = 0
    for i in range(C):
        total += lst[i]
    print(f"#{test_case} {total}")
