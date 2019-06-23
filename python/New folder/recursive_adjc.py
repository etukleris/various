"""def highest(nums):
  out = nums[0]
  for i in nums:
    if i > out:
      out = i
  return (out)"""


def HighNonAdjs(nums):
  out = nums[0]
  for i in range(len(nums)):
    if i <= 1:
      tmp = nums[i] + max(nums[i+2:])
      if ( tmp >= out):
        out = tmp
    else:
      tmp = nums[i] + max(nums[0:i-1] +nums[i+2:])
      if ( tmp >= out):
        out = tmp
  return (out)

nums = [1,2,5,9,99,13,24,69,87,3,-51,123,4,89,10,100,101,45]

print(HighNonAdjs(nums))
