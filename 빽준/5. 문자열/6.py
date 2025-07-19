alphabet = []
for i in range(97,123):
    alphabet.append(chr(i))

word = input('단어를 입력하세요: ')
w_lst = []

for i in range(len(word)):
    w = word[i]
    w_lst.append(w)

for i in alphabet:
    idx = alphabet.index(i)
    if i in w_lst:
        alphabet[idx] = w_lst.index(i)
    elif i not in w_lst:
        alphabet[idx] = -1

print(w_lst)

# AI
# enumerate(리스트) = 리스트의 index와 value를 같이 꺼내오는 메서드
# 문자열 리스트 만들기 → list(word) 매우 간단;
# 문자열 리스트 만들기2 → 컴프리헨션(?) w_lst = [ ch for ch in word ]