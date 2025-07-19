s='aaabbc'
n = {i:s.count(i) for i in list(s)}
r = [''.join(str(w[i]) for i in range(0,2)) for w in n.items()]
print(r)