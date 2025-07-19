N, M = map(int, input('N M :').split(' '))
Ba = []
lst = []

for n in range(N):
    Ba.append(n+1)

for _ in range(M):
    i, j = list(map(int, input('i j : ').split(' ')))
    lst.append([i,j])

for s, e in lst:
    for idx in range(s, ((s+e)//2)+1):
        Ba[idx-1], Ba[s+e-idx-1] = Ba[s+e-idx-1], Ba[idx-1]
        
print(*Ba)

# AI
# 파이썬식 스왑 문법
# list[i], list[j] = list[j], list[i] → list 내의 Index i와 j를 변경
# lst = [[1,2],[2,3]] 등 이중 리스트 일 때, for a,b in lst 로 각 인자를 받아올 수 있음