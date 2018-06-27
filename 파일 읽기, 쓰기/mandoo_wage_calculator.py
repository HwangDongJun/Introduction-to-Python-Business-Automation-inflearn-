class Emplyee:
    name = None
    wage_per_hour = 7530
    work_start = None
    work_finish = None

    def __init__(self, name, work_start, work_finish, wage_per_hour=None):
        self.name = name
        self.work_start = work_start
        self.work_finish = work_finish

        if wage_per_hour != None:
            self.wage_per_hour = wage_per_hour

    def worked_hours(self):
        return self.work_finish - self.work_start

    def wage_of_the_day(self):
        return self.worked_hours() * self.wage_per_hour

e0 = Emplyee('철수', 8, 17)
print(e0.name)
print(e0.work_start)
print(e0.work_finish)
print(e0.wage_per_hour)
print(e0.worked_hours())
print(e0.wage_of_the_day())

print('-----------------------------------------읽는 과정')

f = open('mandoo.csv', 'r') #r로 인해 읽어올 수 있다.
lines = f.readlines() #라인 전부를 읽어오게 된다. list형태로
#len(lines)이면 3을 반환한다.
for n in lines:
    print(n) #안의 값이 반환이 된다.

info1 = lines[1].split(',') #,를 제외하고 각각의 정보들을 넣는다.
info2 = lines[2].split(',')
#-- 이렇게 한개씩 넣는 방법으로 출력이 가능하다.
employee_list = list()
for line in lines:
    info = line.split(',')
    employee_list.append(Emplyee(info[0], info[1], info[2], info[3])) #이렇게 전부 넣는 방법도 가능하다.
f.close()

e1 = Emplyee(info1[0], int(info1[1]), int(info1[2]), int(info1[3]))
print(e1.work_start)
print(e1.work_finish)
print(e1.wage_per_hour)
print(e1.worked_hours())
print(e1.wage_of_the_day())

print("------------------------------")
for w in employee_list:
    print(w.name, w.work_start, w.work_finish, w.wage_per_hour)

#이와 같은 방법으로도 가능하다.

f_output = open('mandoo.csv', 'w')
f_output.write('이름, 출근, 퇴근, 시급\n')
for s in employee_list:
    f_output.write(
        "{},{},{},{}".format(
            s.name, s.work_start, s.work_finish, s.wage_per_hour #같은 내용이지만 이렇게 작성할 수가 있다.
            #새롭게 추가할 수 있다는 의미
        )
    )
