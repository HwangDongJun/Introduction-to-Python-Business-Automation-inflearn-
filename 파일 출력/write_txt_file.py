f = open('first.txt', 'w', encoding='utf-8') #첫번째 인자는 open할 파일 이름, 두번째 인자는 mode인데 w로 write를 나타낸다.
                                                #세번째 인자는 한글출력도 나타내기 위해서 encoding방법을 나타낸 것이다.
                                                #세번째 인자가 이전에 배운 default값으로 설정을 해준것이다.
f.write('hello world\n') #실행을하면 first.txt파일이 생성이되어 hello world라는 글씨가 쓰여지는걸 알 수가 있다.
f.write('hello file\n')
f.write('한글파일 생성')
f.close()

csv = open('csv_test_file.csv', 'w', encoding='utf-8') #파일 확장자가 csv이다. excel파일로 저장이 되어있다.
csv.write('1, 3, 5\n') #csv파일은 구분을 ,로 해준다.
csv.write('7, 9, 11')
csv.close()
#csv => comma seperated values라는 의미