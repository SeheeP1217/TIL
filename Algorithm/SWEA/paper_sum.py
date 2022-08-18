def fac(f):
    if f == 0 or f == 1:
        return 1
    return f * fac(f-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    c = n//2 + 1
    ans = 0
    for i in range(c):
        cnt = 2**i * fac(n-i) / (fac(i)*fac(n-2*i))
        ans += cnt
    print(f"#{tc} {int(ans)}")