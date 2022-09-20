pattern_dic = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    start_r = -1
    for i in range(N):
        if "1" in arr[i]:
            start_r = i
            break
    arr = arr[start_r:start_r + 7]
    end_c = M
    for i in range(M - 1, -1, -1):
        if arr[0][i] == "1":
            end_c = i
            break
    secret_text = arr[0][end_c - 55:end_c + 1]
    solve_list = []
    for i in range(0, 56, 7):
        temp_secret = secret_text[i:i + 7]
        solve_list.append(pattern_dic[temp_secret])
    confirm_number = 0
    for i in range(8):
        if (i + 1) % 2:
            confirm_number += int(solve_list[i]) * 3
        else:
            confirm_number += int(solve_list[i])
    result = 0
    if confirm_number % 10 == 0:
        result = sum(solve_list)
    print(f"#{tc} {result}")