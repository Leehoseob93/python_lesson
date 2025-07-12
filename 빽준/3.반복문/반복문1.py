while True:
    n=int(input('단 수를 입력하세요:'))
    if 9>=n>=1:
        break
    else:
        print(f'단 수를 다시 입력하세요.')

for i in range(1,10):
    print(f'{n} × {int(i)} = {n*int(i)}')