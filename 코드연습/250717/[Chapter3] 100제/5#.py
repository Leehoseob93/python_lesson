words = [ 'apple', 'banana', 'kiwi', 'pear']
words = [w for w in words if 'a' in w]
print(words)

# 문자열의 검색 조건은 문자 내부로도 들어간다 !!
# 'a' in 'banana' → True
# 'ba in 'banana' → True