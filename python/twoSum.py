#/bin/python3

def twoSum(nums, target):
  for i in nums:
      for j in nums:
          if i == target - j:
              return i,j
nums = {2, 7, 11, 15}
target = 9

res = twoSum(nums, target)
print(res)
