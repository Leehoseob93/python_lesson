nums = [1, 2, 3]
lst = ['짝수' if n % 2 == 0 else '홀수' for n in nums]
print(lst)

# 삼항 연산자(ternary operator)
# [CASE1 if n조건1 else CASE2 for n in iterable]
# 기본적으로 elif는 못쓰고 삼항연산자를 중첩해서는 사용 가능
# [CASE1 if n조건1 else CASE2 if n조건2 else CASE3]