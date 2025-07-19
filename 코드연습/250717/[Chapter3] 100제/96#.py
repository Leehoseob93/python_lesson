words = ['abc', 'def', 'ghi']
n = list(map(lambda x : x[::-1], words))
print(n)

# map, filter 등에 요소를 변경하는 함수를 넣어줄 땐, lambda x : x 를 반드시 써줘야합니다.