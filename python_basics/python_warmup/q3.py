'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('input number: '))
# 아래에 코드를 작성해 주세요.

if number % 2 == 0:
    print("even")
else:
    print("odd")

##
if number % 2:
    print("odd")
else:
    print("even")