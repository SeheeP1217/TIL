#버블정렬
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    st = list(map(int,input()))
    lst = bubble_sort(st)
    cnt = [0]*10
    total = 0

    for i in range(N):
        cnt[int(lst[i])] += 1
    for j in range(len(cnt)):
        if cnt[j] >= total:
            total = cnt[j]
            num = j
    print(f"#{test_case} {num} {total}")
    