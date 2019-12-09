# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# O(log n)


def searchRange(nums, target):

    def binarySearch(nums, target, SearchType):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] == target:
                if SearchType == FIRST:
                    if IsInBounds(nums, mid - 1) and nums[mid - 1] == nums[mid]:
                        right = mid - 1
                    else:
                        # Only time this search stops is if we hit the left of the array or
                        # if the element to our left is not us therefore we have the first
                        # occurrence of k
                        return mid
                elif SearchType == LAST:
                    if IsInBounds(nums, mid + 1) and nums[mid + 1] == target:
                        right = mid + 1
                    else:
                        # Only time this search stops is if we hit the left ofthe array or
                        # if the element to our right is not us therefore we have the last
                        # occurrence of k
                        return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    def IsInBounds(nums, index):
        return index >= 0 and index <= len(nums) - 1

    rangeResult = [-1, -1]
    FIRST, LAST = range(2)
    leftBoundIndex = binarySearch(nums, target, FIRST)

    if leftBoundIndex == -1:
        return rangeResult

    rangeResult[0] = leftBoundIndex
    rangeResult[1] = binarySearch(nums, target, LAST)
    return rangeResult


def searchRange2(nums, target):
    def get_start_index(nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def get_end_index(nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid + 1] != target:
                    return mid
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    return [get_start_index(nums, target), get_end_index(nums, target)]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3,4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1 , -1]
