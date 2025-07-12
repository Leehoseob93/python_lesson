dic={}
sum=0
X = int(input('영수증 총 금액:'))
N = int(input('구매한 물건의 종류 수:'))

for i in range(0,N):
    a, b = map(int,input('가격/갯수:').split('/'))
    dic[a]=b
    
for a,b in dic.items():
    sum += a * b

print(f'영수증 금액:{X:,}원 / 실제 금액:{sum:,}원')

if sum == X:

    print(f'O.K')
elif sum != X:
    print(f'N.G')