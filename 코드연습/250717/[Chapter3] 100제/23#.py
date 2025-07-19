scores = {'a':90, 'b':40, 'c':75}
va = {k for k,v in scores.items() if v>=50}
print(va)

# dict는 items() 없이 가져오면 key를 기준으로, key만 출력함.
# dict의 key value를 사용하고 싶다면, k, v in dict.items() 를 사용해줘야함.
# dict를 sorted로 가져올 때, 둘 다 가져오고 싶으면 반드시 dict.items()로 써줘야함!
# dict 만 쓸 경우 key를 기준으로 순회하고, key값만 받아옴.