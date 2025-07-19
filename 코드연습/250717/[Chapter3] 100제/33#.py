nums = [1, 1, 2, 3, 1, 2, 2]
M = max(nums, key = nums.count)
print(M)

# max(iterable, key=함수) → key를 조건으로 iterable 중 가장 큰 수를 반환
# key 에서 함수 자체를 넘기는 것이므로 count()가 아님