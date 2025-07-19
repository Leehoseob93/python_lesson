words = ['hi', 'cat', 'elephant', 'dog', 'ant']
lst = [w for w in sorted(words, key = lambda x : len(x)) if len(w) >=3]
print(lst)