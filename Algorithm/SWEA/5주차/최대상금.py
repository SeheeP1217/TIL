def change(idx, cnt):
    global result
    if cnt == int(c):
        result = max(int(''.join(num)), result)
        return
    for i in range(idx, len(num)):
        for max_idx in range(i + 1, len(num)):
            if num[i] <= num[max_idx]:
                num[i], num[max_idx] = num[max_idx], num[i]
                change(i, cnt + 1)
                num[i], num[max_idx] = num[max_idx], num[i]
    if result == 0 and cnt < int(c):
        rest = (int(c) - cnt) % 2
        if rest == 1:
            num[-1], num[-2] = num[-2], num[-1]
        change(idx, int(c))

T = int(input())
for tc in range(1, T+1):
    num, c = input().split()

    num = list(num)
    result = 0
    change(0, 0)
    print(f"#{tc} {result}")