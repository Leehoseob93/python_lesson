lst = input('주사위 눈을 입력하세요:').split(' ')

for i in set(lst):
    if lst.count(i) == 3:
        print(f'상금: {10000 + int(i)*1000:,}')
        break
    elif lst.count(i) == 2:
        print(f'상금: {1000 + int(i)*100:,}')
        break
    else:
        print(f'상금: {int(max(set(lst)))*100:,}')
        break