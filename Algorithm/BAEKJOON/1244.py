N = int(input())
lst = list(map(int, input().split()))

p = int(input())
for _ in range(p):
    s, c = map(int, input().split())


    if s == 1:
        for i in range(0, N+1, c):
            if i-1 >= 0:
                if lst[i-1] == 0:
                    lst[i-1] = 1
                elif lst[i-1] == 1:
                    lst[i-1] = 0
    elif s == 2:
        if c <= N//2:
            for i in range(c):
                if lst[c-1+i] == 0 and lst[c-1-i] == 0:
                    lst[c-1+i] = 1
                    lst[c-1-i] = 1
                elif lst[c-1+i] == 1 and lst[c-1-i] == 1:
                    lst[c-1+i] = 0
                    lst[c-1-i] = 0
                else:
                    break
        else:
            for i in range(0, N-c+1):
                if lst[c-1+i] == 0 and lst[c-1-i] == 0:
                    lst[c-1+i] = 1
                    lst[c-1-i] = 1
                elif lst[c-1+i] == 1 and lst[c-1-i] == 1:
                    lst[c-1+i] = 0
                    lst[c-1-i] = 0 
                else:
                    break
for i in range(0, N, 20):
    print(*lst[i:i+20])
