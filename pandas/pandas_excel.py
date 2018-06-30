import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
#그래프에 한글을 나타내기 위해서는 해당하는 방법으로 font를 가져와야 하는 것으로 알면 된다.

df = pd.read_excel('mandoo_management.xlsx', sheet_name='Sheet1') #해당하는 excel파일을 읽어오고, sheet_name은 일단 필요하다는 것만 알아두면 된다.
print(df)
print(df['이름']) #일므만 따로 보여주는 것도 가능하다.
print('-----------------------------------------------------')
df['근무시간'] = df['퇴근시간'] - df['출근시간']
df['시간당 만두'] = df['만두생산'] / df['근무시간']
df = df.sort_values(by=['시간당 만두', '근무시간'], ascending=[False, False]) #정렬을 하려고 한다. 정렬을 원하는 값은 by에 표시, ascending-[False]는 내림차순이다.
#2번째 입력들은 시간당 만두가 똑같은 경우가 있기 때문에 그 경우 근무시간을 내림차순으로 정렬을 하게 된다.
print(df)

df.to_excel('result.xlsx', sheet_name='Sheet1') #xlsx파일에 저장하는 방법이다.
print('-----------------------------------------------------')
#현재 df는 print를 통해 확인하면 맨 처음 index가 숫자로 되어있어서 확인이 힘들다. 그래프 상에도 숫자로 표시가 되기 때문에 인위적으로 index를 변경한다.
df = df.set_index('이름') #이와 같은 방법으로 index를 수정할 수 있다.
print(df)
df['시간당 만두'].plot(kind='bar') #bar형태의 그래프를 그리는 방법이다. 해당하는 방법은 원하는 형태를 나타낸 것이지 출력은 할 수가 없다.
plt.savefig('mandoo_per_hour.png') #해당하는 그래프를 저장하는 방법이다.
#주의! savefig는 반드시 show보다 먼저 선언이 되야지 저장이 된다. 만약 show뒤에 올 경우 백지 그림파일만 나타난다.
plt.show(block=True) #이와 같은 방법으로 그래프를 확인할 수 있는데, block=True는 새로운 창을 띄워서 볼 것이냐 라는 의미이다.
