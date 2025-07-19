words = ['apple', 'ant', 'avocado']
# bol = ['True' if i[0] == 'a' else 'False' for i in words]
# print(bol)

taf = all(w.startswith('a') for w in words)
print(taf)

# 문자열 메서드들....
# str.startswith('a') = 첫 글자 'a' 확인
# str.endwith('a') = 끝 글자 'a' 확인
# 'a' in str = a가 있는지 확인
# str.find('a') = a의 위치
# str.count('a') = a의 갯수 확인