def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sm = 0
    bsl = bubble_sort(lst.copy())

    #내림차순이면 break
    if lst == bsl:
        break
    else:
        #리스트에서 최댓값 찾기
        mx = 0
        for i in lst:
            if i > mx:
                mx = i
        #최댓값의 인덱스 값 구하기
        p = 0
        for f in lst:
            if f == mx:
                p = f
                break
            f += 1
        #최댓값까지 차의 합 구하기
        for q in range(len(lst[:p+1])):
            sm += (lst[p+1] - lst[q])
        #lst[p+1:]로 다시 반복
        lst = lst[p:]
    print(f"{tc} {sm}")

