# if sum is 10 this is the target
# loop through the array and store each number and its difference from our sum into a hah table

# [1,4,2,5,6,9]  Target = 9

2 4 6 1 3


#  1 2 3 4 6 target 9
l       r
# O (N) Time O (1) space


def two_sum(nums, target):
    map = {}
    for num in nums:
        if target - num in map:

            return [num, target - num]
        else:
            map[num] = True
    return []

# o(n^2) time | o (n)


def two_sum2(array, target):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if target == firstNum + secondNum:
                return [firstNum, secondNum]
    return []

# (nlogn) time o (1)


def two_sum3(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        sum = array[left] + array[right]
        if sum == target:
            return [array[left], array[right]]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

# Returns the index's


def twoSum(self, nums, target):

    # Numbers that are needed to meet the target will be stored here along with an index of a complementary number.
    wanted_nums = {}

    # Interating through a list of numbers
    for i in range(len(nums)):

        # If number in wanted_nums it means we've got the sum!
        if nums[i] in wanted_nums:
            return [wanted_nums[nums[i]], i]

        # If not, we store the difference (so the number we seek) along with an index
        else:
            wanted_nums[target - nums[i]] = i
