
def binarySearch(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r-l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


def searchMatrix(matrix, target):

    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    l, r = 0, m*n - 1
    while l <= r:

        mid = l + (r - l) // 2
        midEl = matrix[mid // n][mid % n]
        if target == midEl:
            return True
        elif midEl < target:
            l = mid + 1
        elif midEl > target:
            r = mid - 1

    return False


print(searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15))
# print(binarySearch([1, 2, 3, 4, 5, 6, 7], 15))
# print(binarySearch([1, 2, 3, 4, 5, 6, 7], 3))
