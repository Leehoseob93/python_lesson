nums = [4, 2, 4, 3, 2]
# di_num = {idx:num for idx, num in enumerate(nums)}
# di_num.setdefault()
# print(di_num) 뻘짓입니다

n_nums = {n:nums.index(n) for n in nums}
print(n_nums)

# list.index(s) → s가 '처음' 등장하는 idx 값을 가져오는 메서드
