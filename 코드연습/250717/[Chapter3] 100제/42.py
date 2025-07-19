sentence = 'I love natural language processing'
long = [len(i) for i in sentence.rstrip().split()]
print(max(long))