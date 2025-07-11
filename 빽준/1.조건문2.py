while True:
    score = int(input('시험점수를 입력하세요:'))
    if 100>=score>=0:
        print(f'학점을 확인하세요')
        break
    else:
        print(f'올바른 점수를 입력하세요(점수는 0~100점 정수)')

def check(score):
    if score>=90:
        print(f'A')
    elif 90>score>=80:
        print(f'B')
    elif 80>score>=70:
        print(f'C')
    elif 70>score>=60:
        print(f'D')
    else:
        print(f'F')

check(score)