# write a function that moves even intergers to the front and odd integers to the back of the array


def evenOdd(nums):

    nextEven, nextOdd = 0, len(nums) - 1

    while nextEven < nextOdd:
        if nums[nextEven] % 2 == 0:
            nextEven += 1
        else:
            nums[nextEven], nums[nextOdd] = nums[nextOdd], nums[nextEven]
            nextOdd -= 1
    return nums


print(evenOdd([1, 3, 5, 2, 4, 5, 9]))
