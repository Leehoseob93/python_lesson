A, B= map(int, input('시작시간(00:00):').split(':'))
C = int(input('요리시간(m):'))

# B + C / 60 -> 시 + 몫, 나머지 분
# A + 몫 >=24 -> (A+몫)-24

def finish(A,B,C):
    time = (B+C)
    m = time % 60
    h = A + (time // 60)
    if h>=24:
        print(f'종료시간: {h-24}시 {m}분')
    else:
        print(f'종료시간: {h}시 {m}분')

finish(A,B,C)