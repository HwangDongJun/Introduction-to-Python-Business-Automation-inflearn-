import pandas as pd #엑셀파일을 좀 더 자유롭게 다루기 위해서 사용한다.
#as pd는 pandas를 이제부터 pd라는 이름으로 부르겠다는 의미이다.
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]]) #이 방법이 엑셀파일에서 1 2 3
                                                                     #4 5 6  이렇게 입력과 똑같은 것이다.

#아래의 방법을 위에서 바로 할 수 있는데, 그 방법은 df = pandas.DataFrame([[1, 2, 3], [4, 5, 6]],
                                                                        # columns=['aa', 'bb', 'cc'],
                                                                        # index=['x', 'y']
                                                                        # ) 와 같은 방법으로 가능하다.
df.columns = ['aa', 'bb', 'cc'] #행의 0 1 2 의 이름을 정해서 바꾸어 준다.
df.index = ['x', 'y'] #이번엔 첫번째 열의 이름을 바꾸는 방법

df['dd'] = df['aa'] - df['bb'] #새로운 열을 만들어서 그 열의 들어갈 값을 정해주는 방법이다.
df = df.append(df.sum(), ignore_index=True) #df.append로 행의 추가를 할 수 있으며, ignore_index=True로 인해 첫번째 aa~행은 무시하게 된다.
#sum()으로 인해 더한 값이 출력이 된다.
df.index = ['x', 'y', 'sum'] #원래의 값을 잃어버렸기 때문에 다시 설정한다.
print(df)