A_lst = []
B_lst = []
result = []
n = 0
while True:
    A, B = map(int, input('A/B: ').split(' '))
    n += 1
    if A == 0 and B == 0:
        A_lst.append(A)
        B_lst.append(B)
        break
    else:
        A_lst.append(A)
        B_lst.append(B)
        result.append(f'TEST CASE#{n} : {A} + {B} = {A+B}')

print('\n'.join(result))