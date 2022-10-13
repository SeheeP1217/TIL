while True:
    pw = list(input())
    if pw == ['e','n','d']:
        break

    vowel = ['a', 'e', 'i', 'o', 'u']
    possible = 0

    # 모음이 있다면 possible
    for i in pw:
        if i in vowel:
            possible = 1
            break

    # 모음이 3개, 자음이 3개 연속이면 불가능
    for i in range(len(pw)-2):
        if pw[i] in vowel and pw[i+1] in vowel and pw[i+2] in vowel:
            possible = 0
            break
        elif pw[i] not in vowel and pw[i+1] not in vowel and pw[i+2] not in vowel:
            possible = 0
            break

    # 같은 글자가 연속 두번 불가능, ee와 oo는 가능
    for i in range(len(pw)-1):
        if pw[i] == 'o' and pw[i+1] == 'o':
            continue
        if pw[i] == 'e' and pw[i+1] == 'e':
            continue
        if pw[i] == pw[i+1]:
            possible = 0
            break

    ans = ''.join(pw)
    if possible == 1:
        print(f'<{ans}> is acceptable.')
    else:
        print(f'<{ans}> is not acceptable.')
