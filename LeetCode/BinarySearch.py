# O(logn) time |
def binarySearch(array, target):

    mid = (len(array) // 2)
    index = mid

    while index < len(array):
        if target > array[index]:
            index += 1
        elif target < array[index]:
            index -= 1
        else:
            return index


print(binarySearch([1, 2, 4, 5, 10], 5))


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
