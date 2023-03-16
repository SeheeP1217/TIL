K, N= map(int, input().split())

lst = []
sm = 0
for i in range(K):
    num = int(input())
    lst.append(num)
    sm += num

mx_length = sm // N

while mx_length > 0:
    cnt = 0
    for i in lst:
        cnt += i // mx_length
    if cnt < N:
        mx_length -= 1
    else:
        print(mx_length)
        break