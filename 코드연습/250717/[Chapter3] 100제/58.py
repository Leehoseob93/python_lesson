nums = [1, 2, 2, 3]
n = nums.count(2)

di = {str(k):nums.count(k) for k in nums}
print(di)