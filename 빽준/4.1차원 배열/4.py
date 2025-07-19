lst=[]

for _ in lst:
    lst.append(int(input('')))

    M = max(lst)
    M_i = lst.index(M)

print(f'{max(lst)} {M_i}')
