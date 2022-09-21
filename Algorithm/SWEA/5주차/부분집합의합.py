def subset(n, s):
    global K, cnt, visited

    if s == 13 :
        return
 
    a = sum(visited)
    if n == a:
        sm = 0
        for i in range(len(visited)):
            if visited[i] == 1:
                sm += data[i]
        if sm == K:
            cnt+=1
    else:
        visited[s] = 1 
        subset(n, s + 1)
        visited[s] = 0 
        subset(n, s + 1)

TC= int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    cnt = 0
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    visited = [0]*13
    subset(N, 0)

    print(f"#{tc} {cnt}")