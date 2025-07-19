N, X = map(int,input('N X :').split(' '))
lst = list(map(int,input('정수:').split(' ')))
ans = []

for i in lst:
    if i <= X:
        ans.append(i)

print(*ans)

# AI
# 리스트를 출력할때, 쉼표대신 ' ' 을 쓰거나 대괄호를 없애는 방법은??
# 숫자열 리스트의 경우 → *list (리스트형식 제거)
# 문자열일 경우 → '구분자'.join(리스트)
# f'는 포맷팅으로 스트링 형식으로 만드는 것이므로 * 불가능
# '와 { 중첩하면 오류가 발생하기도 한다?? 흠..