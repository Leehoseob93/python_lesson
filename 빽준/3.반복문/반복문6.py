import time
import sys
import io
import random

T = int(input('TEST CASE:'))
fake = ''

#자동 입력 문자열 생성
for _ in range(T):
    lin = f'{random.randint(1,100)}/{random.randint(1,100)}' # A/B 문자열 T개 생성
    fake += lin + '\n'

#1 INPUT 시간 측정

#가짜 입력 주입
sys.stdin = io.StringIO(fake)

A1_lst = []
B1_lst = []
to1 = 0

s1 = time.time()

for i in range(T):
    A1, B1 = map(int, input('').split('/'))
    A1_lst.append(A1)
    B1_lst.append(B1)
    to1 += A1_lst[i] + B1_lst[i]

print(f'{to1}')
# for i in range(T):
#     print(f'{A1_lst[i]} + {B1_lst[i]} = {A1_lst[i] + B1_lst[i]}')

e1 = time.time()

#2 sys.stdin.readline 시간 측정

#가짜 입력 주입
sys.stdin = io.StringIO(fake)

A2_lst = []
B2_lst = []
to2 = 0

s2 = time.time()

for i in range(T):
    A2, B2 = map(int, sys.stdin.readline().rstrip().split('/'))
    A2_lst.append(A2)
    B2_lst.append(B2)
    to2 += A2_lst[i] + B2_lst[i]

print(f'{to2}')

# for i in range(T):
#     print(f'{A2_lst[i]} + {B2_lst[i]} = {A2_lst[i] + B2_lst[i]}')

e2 = time.time()


print(f'실행시간: {e1 - s1:.6f}초') #INPUT 시간
print(f'실행시간: {e2 - s2:.6f}초') #STDIN 시간