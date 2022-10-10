N = int(input())
point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

length = [0, 10]

if (point1[0] + point1[1])/2 < (length[0] + length[1])/2:
    length[0] = (point1[0] + point1[1])/2
else:
    length[1] = (point1[0] + point1[1])/2

if (point2[0] + point2[1])/2 < (length[0] + length[1])/2:
    length[0] = (point2[0] + point2[1])/2
else:
    length[1] = (point2[0] + point2[1])/2

if (point3[0] + point3[1])/2 < (length[0] + length[1])/2:
    length[0] = (point3[0] + point3[1])/2
else:
    length[1] = (point3[0] + point3[1])/2

print(length[1]-length[0])
