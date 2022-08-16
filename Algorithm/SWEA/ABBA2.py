import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(100)]
    lst = []
    for i in range(100):
        for j in range(100):
            lst1 = []
            lst2 = []
            for dj in range(100):
                lst1.append(arr[i][[j+dj]])
            lst2.append(lst1[::-1])
            if lst1 == lst2[0]:
                lst.append(len(lst1))
    for i in range(100):
        for j in range(100):
            lst1 = []
            lst2 = []
            for dj in range(100):
                lst1.append(arr[[j+dj]][i])
            lst2.append(lst1[::-1])
            if lst1 == lst2[0]:
                lst.append(len(lst1))
    mx = 0
    for m in lst:
        if m > mx:
            mx = m
    print(f"#{tc} {mx}")

