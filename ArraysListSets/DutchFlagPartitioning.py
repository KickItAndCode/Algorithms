def dutchFlagPartitioning(pivotIndex, nums):
    pivot = nums[pivotIndex]
    # first pass group elements smaller than the pivit
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break

    for i in reversed(range(len(nums))):
        for j in reversed(range(i)):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break

    return nums


print(dutchFlagPartitioning(3, [0, 1, 2, 0, 2, 1, 1]))
print(dutchFlagPartitioning(2, [0, 1, 2, 0, 2, 1, 1]))
