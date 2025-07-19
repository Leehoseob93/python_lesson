matrix=[[1,2,3],[4,5,6]]
S = [sum(i) for i in list(zip(*matrix))]
print(S)

# *matrix = 언패킹 → 요소들을 풀어서 함수에 넘긴다.
