N = int(input())
ans = -1
for i in range(N//3 + 1):
    if (N - i*3) % 5 == 0:
        ans = i + (N-i*3)//5
        print(ans)
        break
else:
    print(ans)