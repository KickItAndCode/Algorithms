import unittest

#Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers 
# (one from the first array, one from the second array) whose absolute difference is closest to zero. 
# The function should return an array containing these two numbers, with the number from the first array 
# in the first position. Assume that there will only be one pair of numbers with the smallest difference.


# Solution 
# Sort arrays keep track of smallest pairs 
# increment index of left array  if left curr val is less than right array curr val
# opposite if right is larger
# update difference after each run
# return pair
def smallestDifference(arrayOne, arrayTwo):
  smallD = float("inf") #16 12 10 5 

  i = 0; 
  j = 0;
  arrayOne.sort()
  arrayTwo.sort()
  smallestPair = []
  while i < len(arrayOne) and j < len(arrayTwo) :
    ival = arrayOne[i]
    jval = arrayTwo[j]
    diff = abs(ival - jval)
    if (ival < jval):  
      i+= 1
    elif ival > jval:     
      j+= 1
    else:
      return [ival,jval]
    if (diff < smallD ):
      smallD = diff    
      smallestPair = [ival,jval]
  return smallestPair

class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]), [20, 17])
	
	def test_case_2(self):
		self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
	
	def test_case_3(self):
		self.assertEqual(smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031]), [25, 1005])
	
	def test_case_4(self):
		self.assertEqual(smallestDifference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]), [25, 1005])
	
	def test_case_5(self):
		self.assertEqual(smallestDifference([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031]), [2000, 1032])
	
	def test_case_6(self):
		self.assertEqual(smallestDifference([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8]), [954, 954])
	
	def test_case_7(self):
		self.assertEqual(smallestDifference([0, 20], [21, -2]), [20, 21])
	
	def test_case_8(self):
		self.assertEqual(smallestDifference([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]), [1000, 1014])
	
	def test_case_9(self):
		self.assertEqual(smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]), [-123, -124])
	
	def test_case_10(self):
		self.assertEqual(smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]), [530, 530])
	

if __name__ == "__main__":
	unittest.main()

