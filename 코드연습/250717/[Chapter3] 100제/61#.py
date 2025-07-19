matrix = [[1,2,3], [4,5,6], [7,8,9]]
dia = [k[i] for i, k in enumerate(matrix)]
print(dia) # 한 대각선..?

# [matrix[i][i] for i in range(len(matrix))] 더 간단한걸?
