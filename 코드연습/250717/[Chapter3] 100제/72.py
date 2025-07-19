keys = ['a', 'b', 'c']
vals = [1, 2, 3]

di1 ={x[0]:x[1] for x in list(zip(keys,vals))}
di2 =dict(zip(keys,vals))
print(di1)
print(di2)
