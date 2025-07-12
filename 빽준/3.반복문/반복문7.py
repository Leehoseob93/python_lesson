T = int(input('TEST CASE: '))
A_lst = []
B_lst = []
result = []

#1
for i in range(T):
    A, B = map(int, input('A/B: ').split('/'))
    A_lst.append(A)
    B_lst.append(B)
    result.append(f'TEST CASE#{i+1} : {A+B}')

print('\n'.join(result))