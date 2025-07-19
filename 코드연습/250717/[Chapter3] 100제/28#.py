data = { 'x':1 , 'y':2 }
# lst = [k for k in data]
lst = list(data.keys())
print(lst)

# 그냥 dict 값 가져오기.... dict.keys() / dict.values() / dict.items()

print(list(data.keys()))
print(list(data.values()))
print(list(data.items()))