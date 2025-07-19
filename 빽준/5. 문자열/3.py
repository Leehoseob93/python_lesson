T = int(input('TEST CASE: '))
test = []

for _ in range(T):
    te = input()
    test.append(te)

for i in test:
    print(f'{i[0]}{i[-1]}')