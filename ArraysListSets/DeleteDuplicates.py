def deleteDups(nums):
    if not nums:
        return 0

    writeIndex = 1
    for i in range(1, len(nums)):
        if nums[writeIndex - 1] != nums[i]:
            nums[writeIndex] = nums[i]
            writeIndex += 1
    return writeIndex


print(deleteDups([1, 3, 4, 6, 6, 7, 7, 7, 7]))
