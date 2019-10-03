# [12 , 3 , 1 ,2,-6 ,5,-8,  6]
# [-8 , -6, 1, 2, 3, 5, 6, 12] Sorted
#O(n) time |O(n) space
def threeSum (array, target):
  array.sort()
  res = []
  for i in range(len(array)- 2):
    l = i + 1
    r = len(array) -1

    while(l < r):
      currSum = array[i] + array[l] + array[r]
      if currSum == target:
        res.append([array[i], array[l], array[r]])
        l += 1
        r -= 1
      elif currSum < target:
        l += 1  
      else:
        r -= 1
  return res

  
  