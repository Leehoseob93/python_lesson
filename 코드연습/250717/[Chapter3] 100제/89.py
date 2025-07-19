d = {'a': [1], 'b': [2, 3], 'c': []}
nd = [k for k,v in d.items() if len(v) >=2]
print(nd)