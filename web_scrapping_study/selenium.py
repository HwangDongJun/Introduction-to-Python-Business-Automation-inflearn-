#해당하는 방법은 request.py에 추가적인 부분입니다.
#원하는 정보를 가져올려고 하는경우 페이지가 이동할때, 경로 로딩이 걸리면 원하는 정보를 가져오지 못하는 경우가 생기게 된다. 그때 간단한 해결 방법이 selenium이다.
#컴퓨터가 빠르기 때문에 경로 로딩과정에서 정보를 가져오게 되면 당연히 없기 때문에 오류가 발생하는 것이다. => 해결은 13번째 줄
#from selenium import webdirver

#from selenium.webdirver.support.ui import WebDriverWait
#from selenium.webdirver.support import expected_conditions as EC
#from selenium.webdirver.common.by import By
#해당하는 3줄의 사용은 20~22번째줄

#browser = webdriver.Chrome('chromedriver')
#해당하는 오류에 site를 들어가서 운영체제에 맞게 다운로드 파일을 설치한다. 그리고 web_scrapping_sutdy폴더에 추가를 하고, 실행을 시키면 정상적으로 실행된다.
#Chrome브라우저 창이 뜰 것이다.

#정보를 가져오는 코드는 5번째 줄과 browser.quit()사이에 들어가야한다.
#bill_url = 이 부분에 추가적인 정보를 가져와야하는 추가적인 url을 넣는다.
#browser.get(bill_url)  이 코드로 인해 browser에 한번 갔다오는 과정을 거친다.
#browser.implicitly_wait(5) 5초만큼 기다렸다가 가져와라. 이 방법도 원하는 결과를 가져오지 못할 경우도 있다. 랜덤한 경우가 된다.

#WebDriverWait(browser, 10).until(EC.presence_of_element_located(
#   (By.ID, '값이 있는 태그의 id')  이 id가 나올때 까지 browser는 기다려라.
# ))

#html = browser.page_source 페이지의 코드를 가져올 수 있다.
#soup = BeatifulSoup(html, 'lxml')

#body = soup.body 이러한 과정을 거쳐서 원하는 정보를 앞서 request.py에서 했던 방식대로 가져오면 된다.

#body.find(id='~') -> id로 찾는 방법 / body.find_all(tr) -> 태그를 사용해서 찾는방법
#내 생각에는 find의 경우 1개밖에 존재하지 않는 경우이며, find_all은 여러개가 존재할때 찾는 방법인 것 같다.

#browser.quit() 5번째 줄에 의해 창이 뜨고, 이 코드에 의해 뜬 창이 닫히게 된다.