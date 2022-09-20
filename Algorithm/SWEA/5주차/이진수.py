def binary(n):
    if n // 8 == 1:
        lst.append('1')
    else:
        lst.append('0')
    if (n%8) // 4 == 1:
        lst.append('1')
    else:
        lst.append('0')
    if ((n%8)%4) //2 == 1:
        lst.append('1')
    else:
        lst.append('0')
    if ((n%8)%4)%2 == 1:
        lst.append('1')
    else:
        lst.append('0')

T = int(input())
for tc in range(1, T+1):
    N, st = input().split()

    lst = []
    for i in st:
        if i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        binary(int(i))
    print(f"#{tc}", ''.join(lst))
