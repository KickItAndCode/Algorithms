def ElementEqualToItsIndex(nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r-l) // 2
        diff = nums[mid] - mid

        if diff == 0:
            return mid
        elif diff < 0:
            l = mid + 1
        elif diff > 0:
            r = mid - 1
    return -1


print(ElementEqualToItsIndex([1, 2, 3, 4, 4]))
