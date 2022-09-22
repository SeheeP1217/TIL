def move(w, p, sm):
    global ans
    if ans > sm:
        return
    if w == N or p == M:
        if ans < sm:
            ans = sm
        return
    if weight[w] <= possible[p]:
        move(w+1, p+1, sm + weight[w])
    move(w+1, p, sm)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    possible = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    move(0, 0, 0)
    print(f"#{tc} {ans}")