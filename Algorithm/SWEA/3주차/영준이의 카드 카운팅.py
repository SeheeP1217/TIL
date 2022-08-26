T = int(input())
for tc in range(1, T+1):
    card = input()
    lst = []
    lst1 = []
    shp = ['S', 'D', 'H', 'C']
    cnt = [13, 13, 13, 13]
    for i in range(len(card)//3):
        lst.append(card[3*i:3*i+3])
    if len(lst) != len(list(set(lst))):
        print(f"#{tc} ERROR")
        continue
    for a in range(len(card)):
        lst1.append(card[a:a+1])
    for j in range(len(shp)):
        for k in lst1:
            if shp[j] == k:
                cnt[j] -= 1
    print(f"#{tc}", *cnt)




