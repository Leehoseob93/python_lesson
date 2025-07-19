sentence = 'I love natural language processing'
long = [len(i) for i in sentence.rstrip().split()]
print(max(long))
print(max(sentence.rstrip().split(), key = len))

# 33번에 했던거 또 검색함 -_-;
# max(iterable, key=함수) → key를 조건으로 iterable 중 가장 큰 수를 반환
# 즉, 이 문제에서는 sentence를 split으로 쪼갠 list 중 key = len 이 가장 큰 max 를 반환한다...!!