print('나의 돈을 모두 소비할때까지 계란 구입하는 프로그램')

my_money = 10000
egg_price = 300
my_eggs = 0

while my_money > egg_price:
    my_money = my_money - egg_price
    my_eggs = my_eggs + 1
    print('계란 보유: {}개, 남은 돈: {}원'.format(my_eggs, my_money))