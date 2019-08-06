def findThreeLargestNumbers(array):
  res = [None, None, None]
  for num in array:
    if  res[2] is None or num > res[2]:
      res[0] = res[1]
      res[1] = res[2]
      res[2] = num
    elif res[1] is None or  num > res[1]:
      res[0] = res[1]
      res[1] = num
    elif res[0] is None or  num > res[0]:
      res[0] = num
  return res

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))