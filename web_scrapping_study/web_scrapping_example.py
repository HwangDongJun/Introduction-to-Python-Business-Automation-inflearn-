from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello</h1>
</body>
</html>
''' #해당하는 '''내용'''방법은 여러줄을 한꺼번에 넣을 수 있는 방법이다. 즉, 하나의 text로 인지한다. 해당하는 web html파일의 내용 전체를 가져온다.

soup = BeautifulSoup(html, 'lxml') #lxml양식으로 html을 받아오는 것이다.
body = soup.body #soup의 body부분을 가져와라.
h1 = body.h1 #body에서 h1태그만 가져와라.

print(h1.text) #태그까지 전부 출력을 하지말고 내용만 출력을 할때 사용한다.

#table이 있다면 table에서 tbody의 tr인 부분만 출력을 하고 싶다. list를 사용해서
#table = body.table
#tr_list = table.tbdoy.find_all('tr')
#for n in tr_list:
#   print(n)         tbody의 tr에 해당하는 부분을 전부 찾아서 출력한다.
#   print(n.find_all('td')[0].text) 같은 방법도 가능하다.
