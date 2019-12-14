def searchSmallest(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r-l) // 2

        if nums[mid] > nums[r]:
            # min must be in nums[mid +1: right +1]
            left = mid + 1
        else:  # nums[mid] < nums[r]
            right = mid
    return left


# loop ends when left == right
# this only can be solved in less than linear time when values aren't repeated
