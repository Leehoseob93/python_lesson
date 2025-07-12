while True:
    N = int(input('N의 값을 입력하세요(N은 4의배수):'))
    if N % 4 == 0:
        break
    else:
        print(f'N은 4의 배수입니다 -_-')

lo = N // 4
lon = "long "

print(f'{lon * lo}int')