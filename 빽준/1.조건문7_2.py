lst = input('주사위 눈을 입력하세요:').split(' ')
most = max(set(lst),key=lst.count)
count = lst.count(most)

if count == 3:
    print(f'상금: {10000+int(most)*1000:,}')
elif count == 2:
    print(f'상금: {1000+int(most)*100:,}')
elif count == 1:
    print(f'상금: {int(most)*100:,}')
