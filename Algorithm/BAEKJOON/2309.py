a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

short = [a, b, c, d, e, f, g, h, i]
lst = []
for i in range(1<<len(short)):
    sub_lst = []
    for j in range(len(short)):
        if i & (1<<j):
            sub_lst.append(short[j])
    if len(sub_lst) == 7:
        lst.append(sub_lst)

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for a in lst:
    part_sum = 0
    for b in a:
        part_sum += b
    if part_sum == 100:
        print(*bubble_sort(a), sep='\n')
        break
