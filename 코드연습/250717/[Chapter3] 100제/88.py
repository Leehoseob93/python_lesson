nums = [10, 20, 30, 40]

# Method#1 zip을 활용한 방법
mi1 = [y-x for x,y in zip(nums,nums[1:])]
print(mi1)

# Method#2 idx를 활용한 방법
mi2 = [nums[idx+1]-nums[idx] for idx in range(len(nums)-1)]
print(mi2)