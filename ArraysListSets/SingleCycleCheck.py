# # Single Cycle Check

# You are given an array of integers. Each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of 2 indices forward in the array; the integer -3 represents a jump of 3 indices backward in the array. If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0. Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element is visited exactly once before landing back on the starting index.


def hasSingleCycle(nums):
    visited = 0
    currIdx = 0
    while visited < len(nums):
        # found cycle
        if visited > 0 and currIdx == 0:
            return False

        visited += 1
        currIdx = getNextIdx(currIdx, nums)
    return currIdx == 0


def getNextIdx(currIdx, nums):
    jump = nums[currIdx]
    # this handles wrapping around the array
    nextIdx = (currIdx + jump) % len(nums)
    # this handles negative values
    return nextIdx if nextIdx >= 0 else nextIdx + len(nums)


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))  # true
print(hasSingleCycle([2, -1, 1, 2, 2]))  # true
