lst = list(input('두 수를 입력하세요: ').split())
n_lst = []

for i in lst:
    n = list(i)
    n[0], n[2] = n[2], n[0]
    n = int(''.join(n))
    n_lst.append(n)


if n_lst[0] < n_lst[1]:
    print(n_lst[1])
else:
    print(n_lst[0])