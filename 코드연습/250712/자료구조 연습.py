# #1 리스트에서 짝수만 골라 새로운 리스트로 만들기.
# a = [1,2,3,4,5,6]
# b = []

# for i in a:
#     if i % 2 == 0:
#         b.append(i)

# print(f'{b}')


# #2 딕셔너리의 키와 값을 한 줄씩 출력하기.
# a = {'name':'이호섭', 'age':'33세', 'city':'서울'}

# for k, v in a.items():
#     print(f'{k} : {v}')


# #3 리스트의 중복을 제거하고 집합으로 만들기.
# a = [1, 1, 2, 3, 3, 3, 4]
# b = set(a)

# print(f'{b}')


# #4 튜플에서 값을 꺼내 변수로 저장한 후 출력하기.

# a = (3,5)
# x = a[0]
# y = a[1]

# print(f'x:{x} \ny:{y}')


# #5 중첩 리스트 안의 모든 숫자 더하기.

# a = [[1,2],[3,4],[5]]
# sum = 0
# for i in a:
#     for j in i:
#         sum += j

# print(f'{sum}')


# #6 학생정보가 담긴 리스트에서 점수 평균 구하기.

# a = [{'name':'A', 'score':'80'}, {'name':'B', 'score':'90'}, {'name':'C', 'score':'70'}]
# sum = 0
# count = 0

# for i in a:
#     v = i['score']
#     sum += int(v)
#     if 'name' in i:
#         count += 1

# avg = sum / count
# print(f'{avg}')


# #7 두개의 set에서 공통된 요소만 출력하기.

# s1 = {1,2,3}
# s2 = {2,3,4}
# s = set()

# for i in s1:
#     for j in s2:
#         if i == j:
#             s.add(i)

# print(f'{s}')


# #8 튜플로 구성된 리스트에서 최고 점수 찾기

# a = [('A', 85), ('B', 90), ('C', 80)]
# b = max(a, key=lambda x: x[1])

# print(b)


# #9 과목별 점수가 있는 딕셔너리에서 최고 점수 출력

# score = {'python':[90,80,100], 'math':[70,85]}
# # p = score['python']
# # m = score['math']
# t1 = max(score['python']) #p
# t2 = max(score['math']) #m

# print(f'python최고점:{t1}점 \nmath최고점:{t2}점')


# #10 학생별 과목 평균 구하기

# score = {'박인선':{'math':90, 'eng':80}, '이호섭':{'math':70, 'eng':60}}

# p = score['박인선']
# l = score['이호섭']

# # sum1 = 0
# # for v1 in p.values():
# #     sum1 += v1

# # sum2 = 0
# # for v2 in l.vlaues():
# #     sum2 += v2

# to1 = sum(p.values())
# to2 = sum(l.values())

# avg1 = to1 / len(p)
# avg2 = to2 / len(l)

# print(f'박인선 평균: {avg1}점')
# print(f'이호섭 평균: {avg2}점')