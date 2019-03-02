"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):

    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')


# def pair_sum(arr,k):
#     counter = 0
#     lookup = set()
#     for num in arr:
#         if k-num in lookup:
#             counter+=1
#         else:
#             lookup.add(num)
#     return counter
#     pass

def pair_sum(arr,k):

    if len(arr)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k-num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )


    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

#Run tests
t = TestPair()
t.test(pair_sum)
