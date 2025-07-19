words = ['hello', 'hi', 'bye']
m = min(words, key = len)
print(m)

# 33, 49번에 했던거 또 검색함 -_-;
# max(iterable, key=함수) → key를 조건으로 iterable 중 가장 큰 수를 반환
# 즉, 이 문제에서는 sentence를 split으로 쪼갠 list 중 key = len 이 가장 큰 max 를 반환한다...!!
# 다른 종류
# min(iterable, key = 함수) → key 가장 작은 수 반환(dict의 경우 value비교, key반환으로 보임) .. 맞나?
