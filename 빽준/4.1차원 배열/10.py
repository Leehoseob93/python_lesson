N = int(input('시험 본 과목의 개수: '))
score = list(map(int, input('점수를 입력하세요: ').split(' ')))
M = max(score)

for i in score:
  idx = score.index(i)
  score[idx] = (i/M) * 100

# for idx in range(len(score)):
#     score[idx] = (score[idx]/M) *100

avg = sum(score) / len(score)

print(f'{score}')
print(f'평균 점수{avg}')


# 처음에 만든 코드

# for i in score:
#   idx = score.index(i)
#   score[idx] = (i/M) * 100

# 이렇게 할 경우, 60 75 80점을 입력하면 → [0]이 75가 되면서, 75점의 idx를 0으로 가져오므로 [1]의 75점 변환이 안됨

# 인덱스 가져오기 idx = list.index()