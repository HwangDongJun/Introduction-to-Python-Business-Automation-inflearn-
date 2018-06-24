for i in range(0, 10):
    if i % 2 == 0:
        print(str(i) + ' 짝수') #i가 정수인데 string형태가 아니라 str로 캐스팅한다.
        print('{} 짝수'.format(i)) #str사용안하는 방법
    else:
        print(str(i) + ' 홀수')
        print('{} 홀수'.format(i))

print("\n")
for one in range(1, 10):
    for two in range(1, 10):
        print('{} * {} = {}'.format(one, two, one * two)) #구구단