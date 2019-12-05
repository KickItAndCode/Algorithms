def moveElementToEnd(nums, target):

    l, r = 0,  len(nums) - 1

    while l < len(nums) and l < r:
        while nums[l] == target:
            if nums[l] != nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                r -= 1
        l += 1
    return nums


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
print(moveElementToEnd([10, 1, 2, 4, 2, 3, 4, 6], 4))
