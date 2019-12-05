# write a program that takes an array of A of n numbers and rearranges A's elements to get a new array B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] ...

# sort the A and interleave the bottom and top halves of the sorted array
# then swap pairs

# 4 2 5 1 3
# 1 2 3 4 5 Sort
# 2 1 4 3 5 Swap pairs


def rearrange(nums):
    for i in range(len(nums)):
        nums[i:i+2] = sorted(nums[i:i+2], reverse=bool(i % 2))
    return nums


print(rearrange([4, 2, 5, 1, 3]))
