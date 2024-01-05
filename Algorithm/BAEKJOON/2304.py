# 최댓값을 기준으로 좌우로 구분
# 가장자리에 도달할 때까지 최댓값 구분하며 가기

import sys

N = int(input())
arr = [0] * 1001

mx_value = 0
mx_index = 0
for i in range(N):
  L, H = list(map(int, sys.stdin.readline().split()))
  arr[L] = H

  # 최댓값 찾기
  if mx_value < H:
    mx_index = L
    mx_value = H

left_value = 0
right_value = 0
cnt = 0
# 왼쪽
for j in range(mx_index + 1):
  left_value = max(left_value, arr[j])
  cnt += left_value

# 오른쪽
for k in range(1000, mx_index, -1):
  right_value = max(right_value, arr[k])
  cnt += right_value

print(cnt)