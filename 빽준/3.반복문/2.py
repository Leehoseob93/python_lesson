T=int(input('TEST CASE: '))
A_lst=[]
B_lst=[]

for i in range(0,T):
    A, B = map(int,input('A/B를 입력하세요').split('/'))
    A_lst.append(A)
    B_lst.append(B)

for i in range(0,T):
    print(f'{A_lst[i]} + {B_lst[i]} = {A_lst[i]+B_lst[i]}')