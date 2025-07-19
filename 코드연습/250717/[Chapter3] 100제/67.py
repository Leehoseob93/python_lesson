d = {1:'a', 2:'b', 3:'c', 4:'d'}
d = {k:v for k, v in d.items() if k % 2 == 0}
print(d)