"""
Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return [-1, -1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
 """
#[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

# find all unsorted numbers
# compared them to the other numbers # and find position it belonds 

#O(n) time| O (1) space 
def subarraySort(array):

  s = 0
  l = 0
  unsorted = []
  for i  in range(1, len(array)-2):
    # valid spot
    if array[i] > array[i -1] and array[i] < array[ i +1]: 
      continue
    #invalid spot
    else:
      unsorted.append(array[i])

  minNum = min(unsorted)
  maxNum = max(unsorted)
  minIndex = 0
  maxIndex = 0
  for i in range(len(array) -1):
    if (minNum > array[i]):
      continue
    else:
      minIndex = i 
      break
  for i in range(len(array) -1, -1, -1):
    if (maxNum < array[i]):
      continue
    else:
      maxIndex = i  
      break
  return [minIndex, maxIndex]


def subarraySort2 (array):

  minOOO = float("inf")
  maxOOO = float("-inf")

  for i in range(len(array)):
    num = array[i]
    if isOutOfOrder(i, num, array) :
      minOOO = min(minOOO, num)
      maxOOO = max(maxOOO, num)

  if minOOO == float("inf"):
    return [-1, -1]
  l = 0
  r = len(array )-1

  while minOOO >= array[l]:
    l += 1
  while maxOOO <= array[r]:
    r -= 1
  return [l,r]
  
  # find unsorted
  # find index where smallet unsorted should be 
  # find index where largest unnsorte should be
  # return those indexes in array 

def isOutOfOrder(i, num, array):
  if i == 0:
    return num > array[i +1]
  if i == len(array) -1:
    return num < array [i - 1]
 
  return num > array[i +1] or num < array[ i -1] 
  