n = int(input())

arr = [list(input()) for _ in range(n)]

# 가로 확인하기
cntA = 0
cntB = 0
for i in range(n):
    for j in range(n-1):
        if arr[i][j] == '.' and arr[i][j+1] == '.':
            cntA += 1
        
            print(i, j)
            break

for i in range(n):
    for j in range(n-1):
        if arr[j][i] == '.' and arr[j+1][i] == '.':
            cntB += 1
            print(i, j)
            break

print(cntA, cntB)


