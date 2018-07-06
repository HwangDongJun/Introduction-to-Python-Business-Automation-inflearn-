#from bs4 import BeatifulSoup
#import requests 해당하는 방법으로 import한다. 현재 설치는 하지 않았습니다.

#response = resquests.get('scrapping을 원하는 페이지 주소');
#html = response.text

#soup = BeatifulSoup(html, 'lxml')
#body = soup.body  soup을 사용하여 scrapping을 한 페이지 주소 전체의 코드에서 body코드만 가져온다.

#div_ea_list = body.find(id='ea_list')
#print(div_ea_list) 속성중에 id가 ea_list인 태그의 코드를 전부 가져온다.

#table = div_ea_list.table
#tbody = table.tbody 점점 안쪽으로 접근을 시도한다.

#lines = tbody.find_all('tr') tr태그를 모든곳에서 찾아서 넣어라

#bills = list()

#for line in lines:
#   td_list = line.find_all('td')
#   bills.append( [td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text] )

#for  b in bills:
#   print(b) 목록의 정보를 전부 가져올 수 있게 된다.

#pandas를 통해서 excel파일에 담을 수 있다.