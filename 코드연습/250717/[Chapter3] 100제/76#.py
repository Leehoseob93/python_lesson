nums = [1,2,3,4]
sum = [a+b for a,b in zip(nums, nums[1:])]
print(sum)

nums2 = [1,2,3,4]
sum2 = [nums[i] + nums [i+1] for i in range(len(nums2)-1)]
print(sum2)


# 흠.. .. 둘 중에 더 편한 식으로 연습하면 되는건가?