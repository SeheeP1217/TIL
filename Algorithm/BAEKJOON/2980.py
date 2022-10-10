N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t = 0
p = 0

for i in range(N):
    for k in range(p, arr[i][0]+1):
        if k < arr[i][0]:
            t += 1
            p += 1
        if k == arr[i][0]:
            if t % (arr[i][1]+arr[i][2]) < arr[i][1]:
                t += arr[i][1] - t % (arr[i][1]+arr[i][2])
    
print(t+L-arr[N-1][0])
