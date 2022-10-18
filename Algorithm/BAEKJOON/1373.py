N = list(input())
cut = len(N)//3
left = len(N)%3

lst = []
num_8 = []
if left == 2:
    num_8.append(int(N[0]) * 2 + int(N[1]))
    N.pop(0)
    N.pop(0)
elif left == 1:
    num_8.append(int(N[0]))
    N.pop(0)

for i in range(cut):
    lst.append(N[3*i:3*i+3])

for j in range(len(lst)):
    num_8.append(int(lst[j][0])*4 + int(lst[j][1])*2 + int(lst[j][2]))

print(''.join(map(str,num_8)))


