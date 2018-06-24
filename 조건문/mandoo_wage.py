print('만두가게 임금 계산하는 프로그램')
name = '추미애'
work_start = 9
work_finished = 14
worked = work_finished - work_start
wage_per_hour = 7530

if worked >= 4:
    break_time = worked // 4 * 0.5 #4시간마다 0.5의 휴식시간을 가지게 되는데, //의 경우 몫을 구하는 연산자이다.
    worked -= break_time
    print('{}님은 {}시간 근무합니다. 오늘 일당은 {}원 입니다.'.format(name, worked, worked * wage_per_hour))
    print('휴식시간은 {}시간입니다.'.format(break_time))
else:
    print('{}님은 {}시간 근무합니다. 오늘 일당은 {}원 입니다.'.format(name, worked, worked * wage_per_hour))