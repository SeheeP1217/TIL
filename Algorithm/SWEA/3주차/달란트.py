T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    avg = N//P
    rest = N%P
    ans = avg ** (P-rest) * (avg + 1) **(rest)
    print(f"#{tc} {ans}")
