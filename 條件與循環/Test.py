import random

a = random.randint(0, 100)

while True:
    num = int(input('請輸入0~100的數字:'))
    if num == a:
        print('答對了')
        break
    elif num > a:
        print('太大了')
    else:
        print('太小了')
