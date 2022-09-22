T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    A = []
    B = []
    ans = 0
    for i in range(12):
        if i % 2 == 0:
            A.append(lst[0])
            lst.pop(0)
            A.sort()
            for j in range(len(A)-2):
                if ans == 2:
                    break
                if A[j] == A[j+1] == A[j+2]:
                    ans = 1
                    break
                if A[j] in A and A[j]+1 in A and A[j]+2 in A:
                    ans = 1
                    break
        else:
            B.append(lst[0])
            lst.pop(0)
            B.sort()
            for j in range(len(B)-2):
                if ans == 1:
                    break
                if B[j] == B[j+1] == B[j+2]:
                    ans = 2
                    break
                if B[j] in B and B[j]+1 in B and B[j]+2 in B:
                    ans = 2
                    break
    else:
        print(f"#{tc} {ans}")