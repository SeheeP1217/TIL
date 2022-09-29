N = list(input())
ans = []
while len(N) >= 3:
    lst = []
    lst.append(N[len(N)-3:len(N)])
    N.pop(len(N)-3)
    N.pop(len(N)-2)
    N.pop(len(N)-1)
    sm = 0
    for i in range(3):
        sm += int(lst[0][i]) * 2 ** (2-i)
    ans.insert(0, sm)
if len(N) == 1:
    ans.insert(0, int(N[0]))
elif len(N) == 2:
    ans.insert(0, int(N[0])*2+int(N[1]))
print(''.join(map(str, ans)))
