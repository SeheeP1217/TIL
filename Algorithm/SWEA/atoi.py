#def atoi(s):
  #  i = 0
  #  for x in s:
  #      i = i*10 + ord(x)-ord('0')
 #   return i

#print(atoi('123'))
#print(atoi('정수'))

#문자열->정수
st1 = '1234'
sm = 0
for ch in st1:
    sm = sm*10 + (ord(ch)-ord('0'))
print(sm)

#정수->문자열
i = 123
st = ''
while i>0:
    st = chr(i%10 + rod('0'))+st
    i//= 0
print(st)