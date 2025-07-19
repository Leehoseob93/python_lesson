N, M = map(int, input('N M :').split(' '))
Ba = [0] * N

for _ in range(M):
    i, j, k = map(int, input('i j k :').split(' '))
    for n in range(i-1,j):
        Ba[n] = k

print(*Ba)

# AI
# for 