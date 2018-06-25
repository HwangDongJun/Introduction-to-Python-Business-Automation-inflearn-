print('study_function')

def add_two(x): #함수 선언
    y = x + 2
    return y

a = add_two(3)
print(a)

print("\n")

def gugu(x):
    for i in range(0, 10):
        print('{} * {} = {}'.format(x, i, x * i))

gugu(2) #구구단 2단을 출력

print("\n")

def plus_two_items(a, b): #인자가 2개인 함수
    return a + b + b

print(plus_two_tems(2, 3))

print("\n")

def hello_someone(someone):
    return 'hello ' + someone  #숫자뿐 아니라 문자열을 이용

print(hello_someone('기성용'))

print("\n")

def calculator(a, b):
    return a + b, a * b #return 형식을 한개가 아닌 여러개로 가능

sum, mul = calculator(2, 4) #받는 과정에서 순서를 지켜서 받으면 차례대로 받을 수 있다.
print(sum, mul)