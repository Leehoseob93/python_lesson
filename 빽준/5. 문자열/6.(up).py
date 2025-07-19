alphabet = [chr(i) for i in range(97,123)]
w_lst = list(input('단어를 입력하세요: '))

for idx, i in enumerate(alphabet):
    if i in w_lst:
        alphabet[idx] = w_lst.index(i)
    else:
        alphabet[idx] = -1

print(alphabet)

# AI
# enumerate(리스트) = 리스트의 index와 value를 같이 꺼내오는 메서드
# 문자열 리스트 만들기 → list(word) 매우 간단;
# 문자열 리스트 만들기2 → 컴프리헨션(?) w_lst = [ ch for ch in word ]