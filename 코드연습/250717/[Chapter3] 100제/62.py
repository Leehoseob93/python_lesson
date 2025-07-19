matrix = [[1,2,3],[4,5,6],[7,8,9]]
even = [n for w in matrix for n in w if n % 2 == 0]
print(even)