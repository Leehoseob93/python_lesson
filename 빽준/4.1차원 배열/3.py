N = int(input('정수의 갯수:'))
lst = list(map(int,input('정수:').split(' ')))

print(f'{max(lst)} {min(lst)}')
