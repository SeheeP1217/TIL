import sys

N = int(input())

stack = []
for i in range(N):
  a = sys.stdin.readline()
  # print(a)
  stack.append(a)

print(stack)