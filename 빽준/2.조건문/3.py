year=int(input('년도를 입력하세요:'))

if (year % 2 == 0 and year % 100 !=0) or year % 400 == 0:
    print(f'1')
else:
    print(f'0')