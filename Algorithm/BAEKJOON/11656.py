S = str(input())


word = []
for i in range(len(S)):
  word.append(S[i:len(S)])

for j in sorted(word):
  print(j)
