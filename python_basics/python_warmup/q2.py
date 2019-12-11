'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('input number: '))
# 아래에 코드를 작성해 주세요.

i = 0
for i in range(n):
    i = i + 1
    print(i)
    pass

##
for i in range(n):
    print(i + 1)