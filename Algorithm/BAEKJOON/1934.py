A, B = map(int,input().split())

#약수 구해서 합치기
list_AB = []
for i in range(1,A+1):
    if A % i == 0:
        divisor_A = A//i
        list_AB.append(divisor_A)
        

for i in range(1,B+1):
    if B % i == 0:
        divisor_B = B//i
        list_AB.append(divisor_B)

#약수에서 중복 없애기(리스트컴프리헨션 이용)
result = []
#s = set(result)
#result = list(s)
#print(result)
[result.append(x) for x in list_AB if x not in result]
result.remove(A)
result.remove(B)

#리스트의 값 모두 곱하기
def multiply(t):
    ans = 1
    for n in t:
        if n == 0 :
            return 0
        ans *= n
    return ans

print(multiply(result))