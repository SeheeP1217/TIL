T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            lst1 = []
            lst2 = []
            for dj in range(M):
                lst1.append(arr[i][j+dj])
            lst2.append(lst1[::-1])
            if lst1 == lst2[0]:
                print(f"#{tc}", ''.join(lst1))
    for i in range(N):
        for j in range(N-M+1):
            lst1 = []
            lst2 = []
            for dj in range(M):
                lst1.append(arr[j+dj][i])
            lst2.append(lst1[::-1])
            if lst1 == lst2[0]:
                print(f"#{tc}", ''.join(lst1))






