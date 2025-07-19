N = int(input('정수의 갯수:'))
lst = list(map(int,input('정수:').split(' ')))
v = int(input('찾는 정수:'))

print(f'{lst.count(v)}개')

# AI
# map(int,input) 으로만 받으면 리스트로 보이지만 리스트가 아닌 객체로 저장됨
# lst.count() 메서드를 쓸 수 없음.