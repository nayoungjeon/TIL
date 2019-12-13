# Python 기초 문제 정리

## Q1.

###### 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

```python
str = input('input word: ')

print('first : {}'.format(str[0]))
print('last : {}'.format(str[-1]))
```

---

## Q2.

###### 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
n = int(input('input number: '))

i = 0
for i in range(n):
    i = i + 1
    print(i)
    pass

##
for i in range(n):
    print(i + 1)
```

---

## Q3.

###### 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

```python
number = int(input('input number: '))

if number % 2 == 0:
    print("even")
else:
    print("odd")

##
if number % 2:
    print("odd")  # 논리값이 1이라 홀수
else:
    print("even") # 논리값이 0이라 짝수
```

---

## Q4.

###### 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

###### 국어는 90점 이상,

###### 영어는 80점 초과,

###### 수학은 85점 초과,

###### 과학은 80점 이상일 때 합격이라고 정했습니다. (한 과목이라도 조건에 만족하지 않으면 불합격)

###### 다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오.

```python
a = int(input('Kor: '))
b = int(input('Eng: '))
c = int(input('Math: '))
d = int(input('Sci: '))

if a >= 90 and b > 80 and c > 85 and d >= 80:
    print("True")
else:
    print("False") 
```

---

## Q5.

###### 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.

###### 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

###### 입력 예시: 300000;20000;10000

```python
prices = input('input prices: ')


makes = prices.split(";")
p = sorted(makes, reverse = True)
print(p) ## 리스트로 출력됨

##
makes = prices.split(";")
boxes = []
for make in makes:
    boxes.append(int(make))

boxes.sort(reverse = True)
for box in boxes:
    print(box) # 리스트에 들어있는 원소들을 하나씩 출력하기
```

