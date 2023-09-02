"""
바이러스
DFS
"""

import sys

# def dfs(graph, v, visited):
#     visited[v] = True

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

def dfs(k):
    visited[k] = 1
    for j in graph[k]:
        if visited[j]==0:
            dfs(j)


# 첫번째 입력값 - 컴퓨터의 수
n = int(sys.stdin.readline())
# 두번째 입력값 - 연결된 줄의 수
k = int(sys.stdin.readline())

# 그래프 초기화
graph = [[] for i in range(n+1)]
# 방문한 컴퓨터인지 표시
visited=[0]*(n+1)

# 이후 입력값 - k줄 만큼 연결된 컴퓨터 번호 쌍
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a]+=[b]
    graph[b]+=[a]
    

dfs(1)
print(sum(visited)-1)
# a, b, c = map(int, sys.stdin.readline().split())