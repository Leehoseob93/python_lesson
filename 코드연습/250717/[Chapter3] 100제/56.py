s='banana'
w=''.join(i for i in dict.fromkeys(s))
print(w)

e = sorted(set(s))
print(e)