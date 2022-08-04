pw = input()
Big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in pw:
    if i in Big:
        if Big.find(i) < 13:
            result.append(Big[Big.find(i)+13])
        else:
            result.append(Big[Big.find(i)-13])
    elif i in small:
        if small.find(i) < 13:
            result.append(small[small.find(i)+13])
        else:
            result.append(small[small.find(i)-13])
    else:
        result.append(i)

print(''.join(result))