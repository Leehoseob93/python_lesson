matrix = [[1,2], [3,4], [5,6]]
# lst = []
# for i in matrix:
#     for j in i:
#         lst.append(j)
# 컴프리헨션 두번 중첩 가능

lst = [n for r in matrix for n in r]

print(lst)
