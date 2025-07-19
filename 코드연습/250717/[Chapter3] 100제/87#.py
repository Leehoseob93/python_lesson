words = ['Python', 'JAVA', 'go', 'Rust']

u_alpha = [u for x in words for u in x if u.isupper()]
print(u_alpha) #대문자를 다 추출하는 방법

u_alpha2 = [''.join(u for u in x if u.isupper()) for x in words]
print(u_alpha2)

# iterable.isuuper() → 대문자만 추출..
# ''.join(c for c in list if ~) join 뒤에 조건을 걸어서 추가할 문자열을 조절할 수 있음.