for i in range(0, 10): #range사용법 0~9까지 1씩 늘려간다. for사용법도 알아두기
    print(i) #range로 인해 0부터 9까지의 값이 출력 10까지가 아니다.(주의!)

employee_list = ['철수', '맹구', '짱구', '유리', '훈이'] #list선언
birth_list = ['1995', '1996', '1994', '1995', '1999']

for p in employee_list:
    print(p) #list의 값이 차례대로 출력
    print(p + '안녕')

print('\n')
for one in range(0, 5):
    print(employee_list[one], birth_list[one]) #이런식으로도 이용가능