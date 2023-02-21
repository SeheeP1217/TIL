import sys

def visit(a):
    ans = 0
    b = a
    while b > 0:
        if b in visited:
            ans = b
        b//=2
    if ans == 0:
        visited.add(a)
    print(ans)
    
n,q = map(int,input().split())
num = []
visited = set()
for _ in range(q):
    a = int(sys.stdin.readline().rstrip())
    num.append(a)

for i in num:
    visit(i)