st, ft = map(int, input().split())
num_list = []

for i in range(ft+1):
    for j in range(i):
        if len(num_list) == ft:
            break
        num_list.append(i)

print(sum(num_list[st-1:ft]))