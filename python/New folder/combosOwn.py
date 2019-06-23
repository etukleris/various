def deco(numbers, n):
  counts = [0] * (n+1)
  counts [0] = 1
  counts [1] = 1

  for i in range(2, n+1):
    counts[i] = counts[i-1]
    if numbers[i-2] == '1' or (numbers [i-2] == '2' and numbers[i-1] <= '6'):
      counts[i] = counts[i] + counts[i-2] 

  return (counts[n])

  ##
nums = ['1', '1','1', '1', '1','1', '1', '1','1', '1']

print(deco(nums, len(nums)))
