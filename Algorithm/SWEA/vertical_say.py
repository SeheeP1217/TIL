T = int(input())
for tc in range(1, T+1):
    w = [0] * 5
    mx = 0
    for i in range(5):
        w[i] = list(input())
        if len(w[i]) > mx:
            max_len = len(w[i])
    print("#{}".format(tc), end=" ")
    for i in range(mx):
        for j in range(5):
             if len(w[j]) > i:
                 print(w[j][i], end="")

