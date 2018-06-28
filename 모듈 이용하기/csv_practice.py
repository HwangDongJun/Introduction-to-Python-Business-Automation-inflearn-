import csv #csv 모듈 이용

f = open('mandoo.csv', 'r')
lines = csv.reader(f) #기존에 읽는 과정이 필요없고, import로 csv를 사용하기 때문에 이와 같이 사용하면 된다.

for line in lines:
    print(line) #이전에는 split로 나눠야 했지만 이렇게 하면 출력된 결과값에서와 같이 이미 나눠져 있다.

f.close()