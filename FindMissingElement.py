"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal
import collections

class TestFinder(object):

    def test(self,sol):
#assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print ('ALL TEST CASES PASSED')

# def finder(arr1,arr2):
#
#     # Sort the arrays
#     arr1.sort()
#     arr2.sort()
#
#     # Compare elements in the sorted arrays
#     for num1, num2 in zip(arr1,arr2):
#         if num1!= num2:
#             return num1
#
#     # Otherwise return last element
#     return arr1[-1]



def finder(arr1, arr2):
    d1 = dict.fromkeys(arr1)
    print(d1)
    # Using default dict to avoid key errors
    d=collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1

    # Check if num not in dictionary
    for num in arr1:
        if d[num]==0:
            return num

        # Otherwise, subtract a count
        else: d[num]-=1




# Run test
t = TestFinder()
t.test(finder)
