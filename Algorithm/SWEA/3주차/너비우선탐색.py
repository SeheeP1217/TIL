def bfs(s):
    #q, visited, 필요한 flag 초기화
    q = []
    visited = [0]*(V+1)

    #초기데이터를 q에 삽입(+단위작업 ex:visit표시, sol처리)
    q.append(s)
    visited[s] = 1
    sols.append(s)

    #q에 데이터가 있는 동안 반복
    while q:
        s = q.pop(0)    #제일 앞(FIFO)
        #정답처리가 필요한 경우 이 자리에서

        #4,8방향, 연결된 노드, 안 가본 곳 등 조건
        for e in range(1, V+1): #e:끝지점
            #이 문제는 연결된 노드와, 안가본 곳이 조건
            if e in adjL[s] and not visited[e]:
                #위의 초기데이터 단위작업과 똑같이
                q.append(e)
                visited[e] = 1
                sols.append(e)
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    #V:노드 개수 E:엣지 개수

    #인접 리스트에 연결된 노드 추가
    adjL = [[] * (V+1) for _ in range(V+1)] #adjL:인접리스트
    for _ in range(E):
        s, e = map(int, input().split())    #s:시작지점 e:끝지점
        #양방향
        adjL[s].append(e)
        adjL[e].append(s)

    #방문순서대로 sols배열에 추가
    sols = []
    bfs(1)  #1:시작지점
    print(f"#{tc}", *sols)