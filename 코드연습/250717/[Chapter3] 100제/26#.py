s='hellohello'
x=set(list(s))
w = ''.join(i for i in x)
print(w)

# set은 순서가 없으므로 순서 유지가 안됨!

word = 'hellohello'
a = ''.join(dict.fromkeys(word))
print(a)

# dict.fromkeys(iterable) → 중복제거 & 순서유지