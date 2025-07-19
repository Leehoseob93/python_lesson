lst = []

for _ in range(10):
    n = int(input('나누기: '))
    v = n % 42
    lst.append(v)

print(f'{len(set(lst))}')

