nums = [1, 2, 3, 4, 5]
for n in nums[:]:
    if n % 2 !=0:
        nums.remove(n)

print(nums)