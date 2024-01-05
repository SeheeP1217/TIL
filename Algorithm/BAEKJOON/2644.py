"""
촌수계산
DFS
"""

import sys

def dfs(k, num):
    num += 1
    visited[k] = 1

    if k == e:
        result.append(num)

    for j in graph[k]:
        if visited[j]==0:
            dfs(j, num)

n = int(sys.stdin.readline())
s, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited=[0]*(n+1)
result = []

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a]+=[b]
    graph[b]+=[a]

dfs(s, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)