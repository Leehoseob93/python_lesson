nums = [1, 2, 3, 4, 5, 6, 7, 8]
#조건은 3의배수만 반환하는걸로
lst = [n if n % 3 == 0 else 'None' for n in nums]
print(lst)