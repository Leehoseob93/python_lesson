words = ['Hi', 'HELLO', 'python', 'YES']
n_w = [ w.lower() for w in words if len(w)>= 3] # 세 글자 이상 문자열만 소문자로 저장
print(n_w)