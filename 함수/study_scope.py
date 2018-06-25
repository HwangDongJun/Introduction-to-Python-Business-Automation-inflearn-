a = input('input your name:') #사용자의 입력을 기다리게 된다. 실행을 하고 입력을 해서 enter를 치면 아래의 print로 인해 출력이 된다.
#input안에 문자열을 넣으면 문자열 다음에 입력이 가능하다. 사용자 입장에서는 이렇게 입력하는 곳을 확인할 수 있다.

print(a)

print('\n')

def gugu(x):
    for i in range(0, 10):
        print('{} * {} = {}'.format(x, i, x * i))

dan = input('원하는 단을 입력: ') #해당 예시처럼 응용이 가능하다.
print(type(dan)) #해당 dan변수의 type을 알 수 있는 변수 type()을 이용하면 str로 받게 된다.

gugu(int(dan)) #int()함수로 정수형태로 변경