T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]

    #배열에서 암호코드 찾기
    #이미 찾은 중복되는 암호코드 거르기
    lst = []
    for i in range(N):
        pw = ''
        for j in range(M):
            if arr[i][j] != '0':
                pw += arr[i][j]
                if pw in lst:
                    pw = ''
                elif arr[i][j+1] == '0' and pw not in lst:
                    lst.append(pw)
                    pw = ''
    #찾은 암호코드는 이진수로 바꾸기
    lst_2 = []
    for num_16 in lst:
        num_2 = '000000'
        for k in num_16:
            if '0' <= k <= '9':
                n = ord(k)-ord('0')
            else:
                n = ord(k)-ord('A')+10
            for a in range(3, -1, -1):
                num_2 += str((n>>a)&1)
        lst_2.append(num_2)

    #앞뒤 0 개수 제거
    #0을 제거한 암호코드를 7개로 구성하여 10진수로 나타내기
    lst_10 = []
    for z in lst_2:
        num_10 = ''
        ud_10 = ''
        cnt = 0
        for c in range(len(z)):
            if z[len(z)-c-1] == '0':
                cnt += 1
            else:
                break
        for d in range(8):
            st = ''
            st += z[-(cnt) - 7*d -7: -(cnt)-7*d]
            dct = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
            ud_10 += dct[st]
            num_10 = ud_10[::-1]
        lst_10.append(num_10)

    #(홀수자리합*3) + (짝수자리합) + (검증코드)가 10의 배수인 것들의 합 출력
    ans = 0
    for nm in lst_10:
        sm_h = 0
        sm_j = 0
        sm = 0
        for h in range(len(nm)):
            sm += int(nm[h])
            if h % 2 == 0:
                sm_h += int(nm[h])
            else:
                sm_j += int(nm[h])
        total = 3*sm_h + sm_j
        if total % 10 == 0:
            ans += sm
    print(f"#{tc} {ans}")
