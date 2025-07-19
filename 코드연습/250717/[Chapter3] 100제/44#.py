scores = {'Tom':82, 'Jerry':91, 'Bob':78}

# 내 코드
# lst = [v for k,v in scores.items()]

# M = max(lst)
# name = [k for k, v in scores.items() if v == M]
# print(name)

M = max(scores, key = scores.get)
print(M)