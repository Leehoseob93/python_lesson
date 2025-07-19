d = {'b':2, 'a':1, 'c':3}
so = dict(sorted(d.items(), key = lambda x:x[0]))
print(so)

so2 = {v:d[v] for v in sorted(d)}
print(so2)

# 같은 한 줄인데 어떤 코드가 더 좋을까?