T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst1 = []
    lst2 = []
    lst3 = []
    ans = []
    for i in range(N):
        for j in range(N):
            lst1.append(arr[N-1-j][i])
            lst2.append(arr[N-1-i][N-1-j])
            lst3.append(arr[j][N-1-i])
    for a in range(N):
        ans.append(''.join(map(str, lst1[a * N : (a+1) * N])))
        ans.append(''.join(map(str, lst2[a * N : (a+1) * N])))
        ans.append(''.join(map(str, lst3[a * N : (a+1) * N])))
    print(f"#{tc}")
    for b in range(N):
        print(*ans[b*3:(b+1)*3:1])

