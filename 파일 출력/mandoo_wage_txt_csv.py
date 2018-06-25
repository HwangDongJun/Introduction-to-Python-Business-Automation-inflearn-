print('만두가게 임금계산하는 프로그램')
employee_list = ['훈이', '철수', '짱구', '맹구', '유리']
work_start_list = [10, 9, 8, 13, 11]
work_finish_list = [13, 11, 10, 18, 15]

def wage_calculator(worked_hours, wage_per_hour=7530): #함수를 쓰면 좋은점은 같은 문장을 함수 한 군데에 정의를 하고, 이름만 가져다 사용할 수 있는 편리성 제공
    if worked_hours >= 4:
        break_time = worked_hours // 4 * 0.5
        worked_hours = worked_hours - break_time

    wage = worked_hours * wage_per_hour #default값으로 인자에 7530을 써줄수가 있다. 이 같은 경우는 함수를 선언할때 값을 따로 지정하지 않으면 default값이 들어간다.
    return wage

#wage_calculator의 인자를 2개로 받아서 work_finish_list아 work_start_list를 받는 과정부터 진행을 해도 상관은 없다.
#함수를 사용하여 같은 기능을 줄이면 줄일수록 개발자 입장에서는 좋다.

f = open('mandoo_wage.txt', 'w', encoding='utf-8')

for i in range(0, len(employee_list)): #len은 배열의 길이를 출력
    worked = work_finish_list[i] - work_start_list[i]
    wage_of_the_day = wage_calculator(worked) #해당 함수의 경우 wage_per_hour부분을 채우지 않아도 default값이 존재하기 때문에 7530으로 들어간다.
                                              #만약 다른 값을 넣게 된다면 default값이 아닌 채워진 값으로 계산을 한다.
    f.write('{}: {}시간 :: {}원\n'.format(employee_list[i], worked, wage_of_the_day))
    #print대신에 f.write를 사용
f.close() #for문이 끝나고나서 close를 사용하여 닫는다.

#만약 csv파일이었다면 csv.write('{}, {}시간, {}원\n'.format(employee_list[i], worked, wage_of_the_day)) 이렇게 작성하면 된다.
#csv파일같이 excel을 사용할때는 eccoding='utf-8'을 작성하면 안된다. 작성하지 말아야지 한글이 안깨진다.
