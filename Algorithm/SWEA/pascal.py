T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pas = [[1] * a for a in range(1, N+1)]
    for i in range(1, N-1):
        for j in range(len(pas[i])-1):
            pas[i+1][j+1] = pas [i][j] + pas [i][j+1]

    print(f"#{tc}")
    for p in pas:
        print(*p)