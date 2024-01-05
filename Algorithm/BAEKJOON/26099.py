N = int(input())

cnt = -1
mx = N//5

for i in range(mx+1):
  if (N-(mx-i)*5)%3 == 0:
    cnt_3 = (N-(mx-i)*5)//3
    cnt = mx-i + cnt_3
    break



print(cnt)