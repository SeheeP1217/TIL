def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    votes = list(map(int, input().split()))
    for i in range(0, M * 2, 2):
        union_parent(votes[i], votes[i + 1])
    ans = set()
    for i in parent:
        ans.add(get_parent(i))
    print(f"#{tc} {len(ans)-1}")