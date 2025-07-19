stu = 30
yes_n = 28
num = []

for i in range(stu):
    num.append(i+1)

for _ in range(yes_n):
    yes = int(input('과제 한 사람 출석번호: '))
    num.remove(yes)

arr = sorted(num)

print(f'{arr[0]}')
print(f'{arr[1]}')

# AI
# 리스트 제거 방법
# 1. list.remove(n) = '값'을 기준으로 삭제
# 예: lst = [1,2,3,4] → lst.remove(2) = [1,3,4]
# 2. del list[n] = 'idx' 기준으로 삭제
# 예: lst = [1,2,3,4] → del lst[0] = [2,3,4]
# 3. list.pop(n) = 'idx' 기준으로 값을 꺼내면서 삭제
# 예: lst = [1,2,3,4] → val = lst.pop(0) → val = 1 / lst = [2,3,4]