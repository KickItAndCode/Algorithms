# [1,2,5,2,6,7,4] = 5
# [1,3,4,3] = 3
# [a. b, c, a, a,b,c,b,b] = 3
def longestUniqueSubArray (nums):
  l = 0
  r = 0
  valD = {}
  res = 0
  for i in range(len(nums)):
    curr = 0
    if nums[i] in valD:
      l += nums[i] + 1
    else:
      valD[nums[i]]= i
      r += 1
      curr += 1
      res = max(res +1 ,curr )
    print(res)
    return res

  print(longestUniqueSubArray([1,3,4,3]))