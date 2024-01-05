import sys

V, H = map(int, sys.stdin.readline().split())
N = int(input())
cut = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 가로세로 구분
lst_h = []
lst_v = []

lst_h.append(0)
lst_h.append(H)

lst_v.append(0)
lst_v.append(V)

for i in range(N):
    if cut[i][0] == 0:
        lst_h.append(cut[i][1])
    else:
        lst_v.append(cut[i][1])

#정렬된 리스트 안에서 인접한 두 수의 차 중 최댓값
lst_h.sort()
lst_v.sort()
gb_h = []
gb_v = []
for j in range(len(lst_h)-1):
    gb_h.append(lst_h[j+1] - lst_h[j])
for j in range(len(lst_v) - 1):
    gb_v.append(lst_v[j+1] - lst_v[j])

mx_h = 0
mx_v = 0
for a in gb_h:
    if a > mx_h:
        mx_h = a
for b in gb_v:
    if b > mx_v:
        mx_v = b
print(mx_h*mx_v)