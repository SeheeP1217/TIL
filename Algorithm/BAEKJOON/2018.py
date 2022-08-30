N = int(input())

cnt = 0

for i in range(1, N+1):
    sm = 0
    for j in range(i, N+1):
        sm += j
        if sm == N:
            cnt += 1
            break
        elif sm > N:
            break
print(cnt)