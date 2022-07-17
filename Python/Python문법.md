## 알고리즘 문제 해결 시간 

```
  import time
  start_time = time.time()
  end_time = time.time()
  print("time", end_time-start_time)
  ```
  

## 수 자료형
- 유효숫자e^지수 = 유효숫자*10^지수

```
  a = int(2e9)   #정수형 데이터에서 오류가 발생하지 않기 위해 내장함수 int를 사용하는 것이 좋음
  print(a)
```
  
- round 함수
  
```
  b = round(123.456, 2)   #소수 둘째 자리까지 반올림
  print(b)
```

- 몫, 나머지, 거듭제곱 연산자

```
  c = 9 // 2
  print(c) #답은 4

  c = 9 % 2
  print(c) #답은 1

  c = 9 ** 2
  print(c) #답은 81
```


## 리스트 자료형
: 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형

- 비어있는 리스트를 선언 : list()
- 리스트의 원소에 접근할 때는 index 값을 괄호 안에 넣습니다.(인덱스는 0부터 시작)
