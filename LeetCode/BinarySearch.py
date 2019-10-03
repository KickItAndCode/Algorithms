# O(logn) time | 
def binarySearch(array, target):

  mid =  (len(array) //2 )
  index = mid

  while index < len(array):
    if target > array[index]:
      index += 1
    elif target < array[index]:
      index -= 1
    else:
      return index

print(binarySearch([1,2,4,5,10], 5))