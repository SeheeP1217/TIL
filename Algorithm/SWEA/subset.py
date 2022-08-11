T = int(input())
for test_case in range(1, T+1):
    N, total = map(int,input().split())    #부분집합의 원소 개수, 부분집합의 합
    arr = [n for n in range(1, 13)]
    #부분집합 구하기
    result = 0 
    for i in range(1<<len(arr)):
        cnt = 0 #부분집합의 원소 개수
        sm = 0  #부분집합의 합
        for j in range(len(arr)):
            if i & (1<<j):
                sm += arr[j]
                cnt += 1
        if cnt == N and sm == total:
            result += 1
    print(f"#{test_case} {result}")