N = int(input())
point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

length = [0, N]

point1.sort()
point2.sort()
point3.sort()

# 첫 포인트로 접는 선 결정해서 끝선 맞추고 나머지 포인트 위치 재정비

# 접는 선이 중간보다 왼쪽에 있으면 시작점을 이동
if (point1[0] + point1[1])/2 <= (length[0] + length[1])/2:
    length[0] = (point1[0] + point1[1])/2
    # 나머지 포인트 위치 재정비
    # 접는 선이 포인트 사이에 있다면 포인트 이동 / 왼쪽에 모두 있다면 모두 이동 / 오른쪽에 있다면 그대로 두기
    if (point2[0] < length[0] and point2[1] > length[0]):
        point2[0] = length[0] * 2 - point2[0]
        point2.sort()
    elif (point2[0] < length[0] and point2[1] < length[0]):
        point2[0] = length[0] * 2 - point2[0]
        point2[1] = length[0] * 2 - point2[1]
        point2.sort()

    if (point3[0] < length[0] and point3[1] > length[0]):
        point3[0] = length[0] * 2 - point3[0]
        point3.sort()
    elif (point3[0] < length[0] and point3[1] < length[0]):
        point3[0] = length[0] * 2 - point3[0]
        point3[1] = length[0] * 2 - point3[1]
        point3.sort()


# 접는 선이 중간보다 오른쪽에 있으면 끝점을 이동
else:
    length[1] = (point1[0] + point1[1])/2
    # 나머지 포인트 위치 재정비
    # 접는 선이 포인트 사이에 있다면 포인트 이동 / 왼쪽에 모두 있다면 모두 이동 / 오른쪽에 있다면 그대로 두기
    if (point2[0] < length[0] and point2[1] > length[0]):
        point2[0] = length[0] * 2 + point2[0]
        point2.sort()
    elif (point2[0] > length[0] and point2[1] > length[0]):
        point2[0] = length[0] * 2 - point2[0]
        point2[1] = length[0] * 2 - point2[1]
        point2.sort()

    if (point3[0] < length[0] and point3[1] > length[0]):
        point3[0] = length[0] * 2 - point3[0]
        point3.sort()
    elif (point3[0] > length[0] and point3[1] > length[0]):
        point3[0] = length[0] * 2 - point3[0]
        point3[1] = length[0] * 2 - point3[1]
        point3.sort()



if (point2[0] != point2[1]):
    # 접는 선이 중간보다 왼쪽에 있으면 시작점을 이동
    if (point2[0] + point2[1])/2 <= (length[0] + length[1])/2:
        length[0] = (point2[0] + point2[1])/2
        # 나머지 포인트 위치 재정비
        # 접는 선이 포인트 사이에 있다면 포인트 이동 / 왼쪽에 모두 있다면 모두 이동 / 오른쪽에 있다면 그대로 두기
        if (point3[0] < length[0] and point3[1] > length[0]):
            point3[0] = length[0] * 2 - point3[0]
            point3.sort()
        elif (point3[0] < length[0] and point3[1] < length[0]):
            point3[0] = length[0] * 2 - point3[0]
            point3[1] = length[0] * 2 - point3[1]
            point3.sort()


    # 접는 선이 중간보다 오른쪽에 있으면 끝점을 이동
    else:
        length[1] = (point2[0] + point2[1])/2
        # 나머지 포인트 위치 재정비
        # 접는 선이 포인트 사이에 있다면 포인트 이동 / 왼쪽에 모두 있다면 모두 이동 / 오른쪽에 있다면 그대로 두기
        if (point3[0] < length[0] and point3[1] > length[0]):
            point3[0] = length[0] * 2 - point3[0]
            point3.sort()
        elif (point3[0] > length[0] and point3[1] > length[0]):
            point3[0] = length[0] * 2 - point3[0]
            point3[1] = length[0] * 2 - point3[1]
            point3.sort()


if (point3[0] != point3[1]):
    if (point3[0] + point3[1])/2 <= (length[0] + length[1])/2:
        length[0] = (point3[0] + point3[1])/2
    else:
        length[1] = (point3[0] + point3[1])/2


length.sort()


print("{:.1f}".format(length[1]-length[0]))
