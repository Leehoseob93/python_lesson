d = {'a': (1,2), 'b': (3,4)}
avg = {k:(sum(v)/len(v)) for k, v in d.items()}
print(avg)