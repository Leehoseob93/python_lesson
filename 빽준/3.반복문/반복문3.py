while True:
    n=int(input('n값을 입력하세요:'))
    if 10000>=n>=1:
        break
    else:
        print(f'n값을 확인하세요.')

sum=0
for i in range(1,n+1):
    sum += i
    
print(f'1부터 {n}까지의 총 합 = {sum}')