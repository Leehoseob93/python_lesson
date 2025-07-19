dates = ['2021-01-01', '2022-12-25', '2020-07-07']
year = [t[0:4] for t in dates ]
print(year)

year2 = [d.split('-')[0] for d in dates] # 아이디어가 ㄷㄷ 
print(year2)