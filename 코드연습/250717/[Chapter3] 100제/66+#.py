from itertools import groupby

s='aaabbc'

lst = []
for k, g in groupby(s):
    w = f'{k}{len(list(g))}'
    lst.append(w)

print(lst)

ol = [f'{k}{len(list(g))}' for k, g in __import__('itertools').groupby(s)]
print(ol)


# groupby() 연속된 값을 묶는다.
# k, g  = key / iterator
# 컴프리헨션으로 임포트하기 → __import__('itertools').groupby()

# import itertools 를 할 경우 itertools 모듈을 모두 가져오는 것이므로 itertools.groupby() 로 함수를 사용할 수 있음.
# from itertools import groupby 를 할 경우 itertools 모듈에서 groupby함수만 가져온 것이므로, groupby() 함수를 바로 사용할 수 있음.
