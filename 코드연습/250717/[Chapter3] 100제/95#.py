d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
n = [k for k, v in d.items() if list(d.values()).count(v) == 1] # value의 갯수가 1개인 것만 추출.......... idea의 부족

print(n)