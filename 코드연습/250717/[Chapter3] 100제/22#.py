words = ['hi', 'hello', 'a', 'yes']

lst = sorted(words, key = lambda x : len(x))
print(lst)

# sorted(iterable 다 가능, key = lambda)
# sorted 는 무조건 list를 반환한다!