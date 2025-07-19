nums = [1,2,3]
# string = ''.join(str(i) for i in nums) 기존 방법
string = ''.join(map(str,nums)) # map을 사용해보세요

print(string)

