# 779. K-th Symbol in Grammar

# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

# Examples:
# Input: N = 1, K = 1
# Output: 0

# Input: N = 2, K = 1
# Output: 0

# Input: N = 2, K = 2
# Output: 1

# Input: N = 4, K = 5
# Output: 1

# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# Note:

# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].

# Explanation


# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001

# We see that, for any level N, the first half of the string is the same as the string in N-1, the next half is just complement of it. The total number of items in level N is 2^N. The half mark of the string is marked by [2^(N-1)]-th item. So, for any level N:

# if K is in the first half, it is same as the Kth element in level N-1
# if K is in the second half, it is the complement of the number in [K-2^(N-1)]-th position in level N-1
# So, we run the recursion until the base condition (N=1)

def kthGrammar(N, K):
    if N == 1:
        if K == 1:
            return 0
        else:
            return 1

    half = 2**(N-1)
    if K <= half:
        return kthGrammar(N-1, K)
    else:
        res = kthGrammar(N-1, K-half)
        if res == 0:
            return 1
        else:
            return 0


def kthGrammar2(N, K):
    if N == 1 and K == 1:
        return 0

    if kthGrammar2(N-1, (K+1)//2) == 0:
        if K % 2 == 0:
            return 1
        else:
            return 0
    else:
        if K % 2 == 0:
            return 0
        else:
            return 1

# Our base case is N = 1 and K = 1.
# Given N, K, we really just need to look up what value is at row N-1, index floor((k+1)/2)). This value in the previous row would have been replaced to generate our current row. So if this value is 0, then it would have been replaced with "01", and depending on whether K is even or odd we can figure out which digit it is. (same idea if the value in the previous row is 1)

# You can try out with a few examples to see the math.


print(kthGrammar2(1, 1))  # 0
print(kthGrammar2(2, 1))  # 0
print(kthGrammar2(2, 2))  # 1
print(kthGrammar2(4, 5))  # 1
