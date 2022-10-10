arr = [list(map(int, input().split())) for _ in range(4)]

visited = [[0]* 100 for _ in range(100)]

for i in range(4):
    for y in range(arr[i][1], arr[i][3]):
        for x  in range(arr[i][0], arr[i][2]):
            visited[y][x] = 1

sm = 0
for a in range(100):
    for b in range(100):
        sm += visited[a][b]

print(sm)