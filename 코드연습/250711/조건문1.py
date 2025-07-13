#1번
# A = 5
# B = 5

# if A>B:
#     print("A>B")
# elif A<B:
#     print("A<B")
# else:
#     print("A=B")

#2번
# score = int(input("시험점수를 입력하세요:"))

# if score>=90:
#     print("A")
# elif 80<=score<=89:
#     print("B")
# elif 79>=score>=70:
#     print("C")
# else:
#     print("F")

#3번
#윤년은 연도가 (4의 배수이면서, 100의 배수가 아닐 때) 또는 (400의 배수일 때)이다.
yoon=100

if (yoon % 4 == 0 and yoon % 100 !=0) or (yoon % 400 ==0):
    print("1")
else:
    print("0")
