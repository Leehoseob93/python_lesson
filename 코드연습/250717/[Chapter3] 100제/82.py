d = {'a': 2, 'b': 5, 'c': 3}

n_d = [k for k, v in sorted(d.items(), key = lambda x : x[1], reverse=True)]
print(n_d)
