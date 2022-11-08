N = int(input())
jump = []
mn_energe = [5000]*N    # 최소 에너지 배열 생성
mn_energe[0] = 0
for i in range(N-1):
    # 작은 점프, 큰 점프만
    s, b = map(int, input().split())
    jump.append((s, b))
    if i+1 < N:
        mn_energe[i+1] = min(mn_energe[i+1], mn_energe[i]+s)
    if i+2 < N:
        mn_energe[i+2] = min(mn_energe[i+2], mn_energe[i]+b)

#매우 큰 점프
vb = int(input())
mn_vb = mn_energe[-1]
for i in range(3, N):
    e, mn_energe1, mn_energe2 = mn_energe[i-3]+vb, 5000, 5000
    for j in range(i, N-1):
        if i+1 <= N:
            mn_energe1 = min(mn_energe1, e+jump[j][0])
        if i+2 <= N:
            mn_energe2 = min(mn_energe2, e+jump[j][1])
        e, mn_energe1, mn_energe2 = mn_energe1, mn_energe2, 5000
    mn_vb = min(mn_vb, e)
print(mn_vb)

