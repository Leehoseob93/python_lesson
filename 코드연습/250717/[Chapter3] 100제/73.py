a = [1, 2, 3]
b = [1, 0, 3]

# 문제에서 제시한 결과는 같으면 SAME 다르면 DIFFERENT 출력

sad = ['SAME' if x == y else 'DIFFERENT' for x,y in zip(a,b)]
print(sad)