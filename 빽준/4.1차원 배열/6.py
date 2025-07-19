N, M = map(int, input('N M :').split(' '))
Ba = []
for n in range(N):
    Ba.append(n+1)

for _ in range(M):
    i, j = map(int, input('i j :').split(' '))
    Ba[i-1], Ba[j-1] = Ba[j-1], Ba[i-1]


print(*Ba)

# AI
# 파이썬식 스왑 문법
# list[i], list[j] = list[j], list[i] → list 내의 Index i와 j를 변경