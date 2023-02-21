def draw(n,j):
    if n==1:
        stars[j][j] = '*'
        return
    l = 4*n-3

    for i in range(j,l+j):
        stars[j][i]='*'
        stars[j+l-1][i]='*'

        stars[i][j]='*'
        stars[i][j+l-1]='*'

    return draw(n-1,j+2)

n = int(input())
cnt = 4*n -3

stars = [[' ']*cnt for _ in range(cnt) ]

draw(n,0)

for i in range(cnt):
    for j in range(cnt):
        print(stars[i][j],end="")
    print()