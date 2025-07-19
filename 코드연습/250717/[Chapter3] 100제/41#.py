a = [1,2,3,4]
b = [5,6,7,8]
sum = [sum(y) for x, y in enumerate(zip(a,b)) if x % 2 == 0]
print(sum)

# 어렵드아
# x+y 값을 sum에 반환하는데,
# i인덱스인 값만 반환한다.
# enumerate를 통해, 인덱스와 튜플 값을 뽑아내는데 → i, (x,y)로 idx / tuple 내 인자를 정해 줄 수 있고 // x, y in enu~ 로 인덱스 x 튜플 전체 y로 뽑은 다음 sum을 해도 되는듯?
