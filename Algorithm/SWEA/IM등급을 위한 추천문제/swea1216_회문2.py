for tc in range(1, 11):
    T = int(input())
    arr1 = [list(input()) for _ in range(100)]
    arr2 = list(map(list, zip(*arr1)))
    lst = []
    for k in range(100):
        for i in range(100):
            for j in range(k+1):
                a1 = arr1[i][j:j+100-k]
                a2 = a1[::-1]
                b1 = arr2[i][j:j+100-k]
                b2 = b1[::-1]
                if a1 == a2:
                    lst.append(len(a1))
                if b1 == b2:
                    lst.append(len(b1))
    print(f"#{tc} {max(lst)}")