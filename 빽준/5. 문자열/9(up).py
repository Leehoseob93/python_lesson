lst = input('두 수를 입력하세요: ').split()
n_lst = [int(i[::-1]) for i in lst]
print(f'{max(n_lst)}')

# AI
# 숫자는 str로 했다가 이어붙여서 int로 정수로 또 만들 수 있음 !
# 문자열 뒤집기 더 쉬운방법 → n_lst = [int(i[::-1]) for i in lst]