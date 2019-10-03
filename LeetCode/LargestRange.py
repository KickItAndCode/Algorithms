import unittest


#Write a function that takes in an array of integers and returns an array of length 2 
# representing the largest range of numbers contained in that array. The first number 
# in the output array should be the first number in the range while the second number
#  should be the last number in the range. A range of numbers is defined as a set of 
# numbers that come right after each other in the set of real integers. For instance,
#  the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of
# \ length 5. Note that numbers do not need to be ordered or adjacent in the array in
#  order to form a range. Assume that there will only be one largest range.

# Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
               #[0, 1,  2, 3, 4, 5, 6, 7, 10 ,11, 12, 15]


# def largestRange(array):
#   res = [0,0]
#   array.sort()
#   l = 0
#   r = 1
#   currIdx = 0
#   lval = array[l]
#   rval = array[r]
#   while l < len(array) and r < len(array):
#     if lval < rval and array[currIdx] + 1 == rval:
#         if (abs(res[0] - res[1] < abs(lval - rval))):
#           res = [lval, rval]
#        currIdx +=1
#         r += 1
#     else: 
#         l += 1
#         r += 1
#   return res

# O (N) time | O (N) space
def largestRange(array):
  bestRange = []
  longestLength = 0
  nums = {}

  # assign all values to hashmap and set to true
  for num in array:
    nums[num] = True

  for num in array:
    #skip numbers that are inside the maps already to only visit once
    if not nums[num]:
      continue
    
    nums[num] = False
    currentLength = 1
    left = num -1
    right = num + 1
    
    #look to the left of the number and stop when the number isnt in the map anymore 
    # update counts
    while left in nums:
      nums[left] = False
      currentLength += 1
      left -= 1

    #look to the right of the number and stop when the number isnt in the map anymore 
    # update counts
    while right in nums:
      nums[right]= False
      currentLength += 1
      right += 1

    # update new latest best range
    if  currentLength > longestLength:
      longestLength = currentLength
      bestRange = [left +1 , right -1]
    return bestRange

class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(largestRange([1]), [1, 1])

	def test_case_2(self):
		self.assertEqual(largestRange([1, 2]), [1, 2])

	def test_case_3(self):
		self.assertEqual(largestRange([4, 2, 1, 3]), [1, 4])

	def test_case_4(self):
		self.assertEqual(largestRange([4, 2, 1, 3, 6]), [1, 4])

	def test_case_5(self):
		self.assertEqual(largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1]), [6, 10])

	def test_case_6(self):
		self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])

	def test_case_7(self):
		self.assertEqual(largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]), [10, 19])

	def test_case_8(self):
		self.assertEqual(largestRange([0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]), [-1, 19])

	def test_case_9(self):
		self.assertEqual(largestRange([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]), [-7, 7])

	def test_case_10(self):
		self.assertEqual(largestRange([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]), [-7, 7])

	def test_case_11(self):
		self.assertEqual(largestRange([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]), [-8, 19])


if __name__ == "__main__":
	unittest.main()
