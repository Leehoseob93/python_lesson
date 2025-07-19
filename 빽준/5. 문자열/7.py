T = int(input('TEST CASE: '))
result = []

for _ in range(T):
    R, S = input('R S: ').split(' ')
    R = int(R)
    word = ''
    for w in S:
        word += w*R
    result.append(word)

for re in result:
    print(re)


# AI
# string 이어붙이기 ~ += 으로도 가능
# 굉장히 어려웠삼