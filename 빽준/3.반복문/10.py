N = int(input('별 갯수:'))
st = '*'
sp = ' '

for i in range(N):
    print(f'{sp * (N - (i+1)) + st*(i+1)}')