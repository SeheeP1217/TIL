def combination(arr, r):

    result3 = []
    def combinate(c, index, index2):
        if len(c) == r:
            result = []
            result.append(c)
            c2 = []
            for idx, data in enumerate(arr):
                if idx not in index2:
                    c2.append(arr[idx])
            result.append(c2)
            result3.append(result)
            return

        for idx, data in enumerate(arr):
            if idx > index:
                combinate(c+[data], idx, index2 + [idx])


    combinate([], -1, [])

    return result3


T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input()))
    ans = 0
    combination(N, 3)
    for r in combination(N, 3):
        if r[0][0] == r[0][1] == r[0][2] or r[0][0] + 2 == r[0][1] + 1 == r[0][2]:
            if r[1][0] == r[1][1] == r[1][2] or r[1][0] + 2 == r[1][1] + 1 == r[1][2]:
                ans = 1
                break
    print(f"#{tc} {ans}")
                
