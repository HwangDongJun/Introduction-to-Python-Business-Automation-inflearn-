class EmployeeList: #클래스를 만들때는 첫번째 문자를 대문자로 시작
    name = "-"
    wage_per_hour = 7530
    work_start = None
    work_finish = None #아무것도 없다라는 의미 -> None

    def __init__(self, name, work_start, work_finish): #생성자를 의미
        self.name = name
        self.work_start = work_start
        self.work_finish = work_finish

    def worked_hours(self): #self는 클래스안에 만드는 함수는 반드시 들어가야한다.
        return self.work_finish - self.work_start  #self는 this의 의미와도 같다.

    def wage_of_the_day(self):
        return self.worked_hours() * self.wage_per_hour

#클래스안에는 변수도 넣을 수 있으며, 함수도 넣을 수가 있다.
#클래스란 자료형태를 담는 틀이며, instance의 경우 그 틀로 찍어내는 값을 의미한다. (아랫부분 참고)

e0 = EmployeeList('짱구', 9, 18) #자료형태를 담는 클래스의 name에 값을 넣게 된다. -> 생성자를 이용
print(e0.name) #그 값을 출력하게 된다.
print(e0.wage_per_hour)
print(e0.work_start)
print(e0.work_finish)
print(e0.worked_hours())
print(e0.wage_of_the_day())

e1 = EmployeeList('철수', 10, 19)
print(e1.name)
print(e1.wage_per_hour) #e0와 e1은 다른 것이다.
print(e1.work_start)
print(e1.work_finish)
print(e1.worked_hours())
print(e1.wage_of_the_day())

#---------------------------------------------------------------------------------------------------
employee_list = list() #이와같은 방법으로 list선언이 가능하다. []로 선언도 가능은 하지만 list()가 더 좋은 방법
employee_list.append(EmployeeList('짱구', 9, 18))
employee_list.append(EmployeeList('철수', 10, 19))

for e in employee_list:
    print("\n{}\t{}\t{}\t{}\t{}\t{}\t".format(e.name, e.wage_per_hour, e.work_start, e.work_finish, e.worked_hours(), e.wage_of_the_day()))

#이와 같은 방법으로도 가능하다.
#---------------------------------------------------------------------------------------------------
f = open('employee_list.csv', 'w')

f.write("이름, 시급, 출근, 퇴근, 근무시간, 일당\n")
for w in employee_list:
    f.write("{}, {}, {}, {}, {}, {}\n".format(w.name, w.wage_per_hour, w.work_start, w.work_finish, w.worked_hours(), w.wage_of_the_day()))

f.close()