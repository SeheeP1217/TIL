T = int(input())
for tc in range(1, T+1):
    dct1 = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0100', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    dct2 = {'001101':'0', '010011':'1', '111011':'2', '110001':'3', '100011':'4', '110111':'5', '001011':'6', '111101':'7', '011001':'8', '101111':'9'}

    st1 = input()
    st2 = ''
    ans = []
    for ch in st1:
        st2 += dct1[ch]
    cnt = 0
    for c in range(len(st2)):
        if st2[len(st2)-c-1] == '0':
            cnt += 1
        else:
            break
    for i in range((len(st2)-2*cnt)//6):
        st3 = ''
        st3 += st2[6*i+cnt:6*i+cnt+6]
        ans.append(dct2[st3])

    print(f'#{tc}', *ans)

