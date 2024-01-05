"""
올림픽 메달로 순위 매기기

1. 금메달 수가 더 많은 나라
2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

[input type]
4 3             // 첫 줄은 국가의 수 N과 등수를 알고 싶은 국가 K
1 1 2 0         // N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 금,은,동메달의 수
2 0 1 0         // 만약 같으면 둘은 같은 등수이고 다음 등수는 생략
3 0 1 0
4 0 0 1

[output type]
2

[내 풀이]
1. 등수를 알고 싶은 국가보다 금메달이 많은 국가 수 알기
2. 등수를 알고 싶은 국가와 같은 금메달 수인 국가들 중 은메달이 더 많은 국가 수 알기
3. 등수를 알고싶은 국가와 같은 은메달 수인 국가들 중 동메달이 더 많은 국가 수 알기
"""

import sys


N, K = map(int, sys.stdin.readline().split())


cnt = 1

arr = []
for i in range(N):
  lst = list(map(int, sys.stdin.readline().split()))

  if lst[0] == K:
    a = lst[1]
    b = lst[2]
    c = lst[3]
    K_lst = [a, b, c]
  else:
    arr.append(lst)


# for i in arr:
#   if i[1] > a:
#     cnt += 1
#     arr.remove(i)
#   elif i[1] < a:
#     arr.remove(i)

# for i in arr:
#   if i[2] > b:
#     cnt += 1
#     arr.remove(i)
#   elif i[2] < b:
#     arr.remove(i)

# for i in arr:
#   if i[3] > c:
#     cnt += 1
#     arr.remove(i)
#   elif i[3] < c:
#     arr.remove(i)



for i in range(1,4):
  remove_arr = []
  for j in range(len(arr)):
    if arr[j][i] > K_lst[i-1]:
      cnt += 1
      # arr.remove(arr[j])
      remove_arr.append(arr[j])
    elif arr[j][i] < K_lst[i-1]:
      # arr.remove(arr[j])
      remove_arr.append(arr[j])
  for k in range(len(remove_arr)):
    arr.remove(remove_arr[k])

print(cnt)