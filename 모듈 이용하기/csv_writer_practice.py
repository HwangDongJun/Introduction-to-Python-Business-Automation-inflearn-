import csv

f = open('mandoo.csv', 'w', newline='') #writerow의 경우 \n이 들어가있어서 한칸이 떨어진 상태로 들어가는데 newline=''로 하게 되면 새로운 라인을 없어지기 때문에 중간에 빈 공간이 사라진다.
csv_writer = csv.writer(f)

csv_writer.writerow(['첫번째', '두번째', '세번째', '네번째']) #writerow는 한줄을 쓰겠다는 의미이다.
csv_writer.writerow([1, 2, 3, 4])

f.close()