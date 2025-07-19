text = 'map filter reduce lambda'
dic = {k:len(k) for k in text.split()}
print(dic)

# {w: len(set(w)) for w in text.split()} → 정답은 이건데.. set하면 알파벳이 중복될 경우 사라지니까 안되는거 아닌가요?!
