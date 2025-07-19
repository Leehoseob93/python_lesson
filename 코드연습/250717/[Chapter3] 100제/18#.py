word = 'education'
w_new = ''.join([w for w in word if w not in 'aeiou'])
print(w_new)

# 문자열을 하나씩 검색할땐, != 이 아닌 not in을 사용해야함