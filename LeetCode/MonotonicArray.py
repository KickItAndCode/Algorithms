# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.


# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true

def isMonotonic(A):
    allIncreasing = True
    allDecreasing = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i+1]:
            allIncreasing = False

    for i in range(0, len(A) - 1):
        if A[i] < A[i + 1]:
            allDecreasing = False

    return allDecreasing | allIncreasing


def isMonotonic(self, A):
    increasing = decreasing = True

    for i in xrange(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing


print(isMonotonic([1, 2, 2, 3]))  # true
print(isMonotonic([6, 5, 4, 4]))  # true
print(isMonotonic([1, 3, 2]))  # false
print(isMonotonic([1, 1, 1]))  # true
