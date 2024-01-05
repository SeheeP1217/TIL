from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
  order = input()

  order_str = order[:3]

  if (order_str == "pus"):
    queue.append(int(order[5:]))
  
  elif (order_str == "pop"):
    if (len(queue) != 0):
      print(queue[0])
      queue.popleft()
    else:
      print(-1)

  elif (order_str == "siz"):
    print(len(queue))

  elif (order_str == "emp"):
    if (len(queue) == 0):
      print(1)
    else:
      print(0)

  elif (order_str == "fro"):
    if (len(queue) == 0):
      print(-1)
    else:
      print(queue[0])

  elif (order_str == "bac"):
    if (len(queue) == 0):
      print(-1)
    else:
      print(queue[-1])