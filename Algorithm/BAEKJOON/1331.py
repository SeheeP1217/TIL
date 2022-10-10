N = [input() for _ in range(36)]

ans = 'Valid'
if len(set(N)) != 36:
    ans = 'Invalid'
for a in range(len(N)):
    if N[a][0] == 'A':
        N[a] = '1' + N[a][1]
    elif N[a][0] == 'B':
        N[a] = '2' + N[a][1]
    elif N[a][0] == 'C':
        N[a] = '3' + N[a][1]
    elif N[a][0] == 'D':
        N[a] = '4' + N[a][1]
    elif N[a][0] == 'E':
        N[a] = '5' + N[a][1]
    elif N[a][0] == 'F':
        N[a] = '6' + N[a][1]
N.append(N[0])
for i in range(36):
    if abs(int(N[i][0]) - int(N[i+1][0])) == 2 and abs(int(N[i][1]) - int(N[i+1][1])) == 1:
        continue
    if abs(int(N[i][0]) - int(N[i+1][0])) == 1 and abs(int(N[i][1]) - int(N[i+1][1])) == 2:
        continue
    else:
        ans = 'Invalid'
print(ans)

