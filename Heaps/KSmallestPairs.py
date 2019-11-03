# 373. Find K Pairs with Smallest Sums

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair(u, v) which consists of one element from the first array and one element from the second array.

# Find the k pairs(u1, v1), (u2, v2) ...(uk, vk) with the smallest sums.

# Example 1:

# Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
# Output: [[1, 2], [1, 4], [1, 6]]
# Explanation: The first 3 pairs are returned from the sequence:
#     [1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]
# Example 2:

# Input: nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2
# Output: [1, 1], [1, 1]
# Explanation: The first 2 pairs are returned from the sequence:
#     [1, 1], [1, 1], [1, 2], [2, 1], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]
# Example 3:

# Input: nums1 = [1, 2], nums2 = [3], k = 3
# Output: [1, 3], [2, 3]
# Explanation: All possible pairs are returned from the sequence: [1, 3], [2, 3]


# consider two input arrays:
# nums1=[a1,a2,a3]
# nums2=[b1,b2,b3]

# and let's say k=3

# We know the brutal force way to do it is to calc (a1, b1), (a1, b2),
# (a1,b3)....(a3,b3)'s sum respectively and sort the sums, and pick
# the top 3 of them. This algorithm is O(n2). And we need an algorithm
#  better than that.

# So, the overall idea of the algorithm:
# Maintain a min-heap to keep only part of the whole set of combinations
# of all elements from nums1 and nums2. That way, we can avoid the brutal
# force way which is O(n2). We only push necessary pairs into the heap,
#  until we find all of the k pairs.

# How we achieve that (for the sake of explanation, ignore the corner cases for now):
# 1, create a heap, then push (S0, N1, N2) into the heap, where N1 is the position of first element in nums1, N2 is the position of first element in nums2, S0 is the sum of N1 and N2. Mark (N1,N2) as visited.
# 2, Pop the root element (S0, N1,N2) out of the heap, add (N1,N2) to the result to be returned. and immediately push (S1, N1+1,N2) and (S2, N1, N2+1) into the heap, where S1 = nums1[N1+1]+nums2[N2], S2 = nums1[N1] + nums2[N2+1]. Here, if a pair (Nx, Ny) has already been visited, we'll ignore it and not push it to the heap.
# 3, repeat this, until all k pairs have been added into the return list. Return the list.

# The complexity of this algorithm is O(klgk) if k<n, because we repeat k times, and each time we do a O(lgk) heappush.

# Why this algorithm works? The real question is, in this algorithm, how do we know that the sum of the pair that got heappopped earlier is always smaller than the sum of any pair that got heappushed later. Why we so sure about that?

# Because, look at the process:
# We heappop the minimal pair (S0, N1, N2), then immediately heappush two larger pairs (S1, N1+1,N2) and (S2, N1, N2+1). (why S1 and S2 always larger than S0? Because the two arrays are sorted.) And right after the heappush, the heap gets re-heaped, and of course the root at this point is larger (at least equal) than (S0, N1, N2). Remember though, the root now maybe (S1, N1+1,N2) or (S2, N1, N2+1) or any other pair that already exists in the heap after that heappop operation. This process gets repeated over and over again until finished.

# From this, we can conclude that, the pairs that get heappushed is always larger than the pairs that get heappopped earlier. It might be smaller than other pairs that are currently in the heap, but we don’t care about that. We only care about pairs that got pushed or popped.

# The beauty of this algorithm is, it works perfectly under the fact: two array are sorted. If the arrays were to be unsorted, we would not be able to guarentee that the two pairs get heappushed are always larger than the pair that gets heappopped, thus it would be possible that a pair that gets heappopped later is larger than one gets heappopped ealier, which would fail to produce the correct answer.


from heapq import *


def kSmallestPairs(nums1, nums2, k):
    # key sum value list of list for pairs
    if not nums1 and not nums2:
        return []

    map = {}
    for num1 in nums1:
        for num2 in nums2:
            sum = num1 + num2
            if sum not in map:
                map[sum] = [[num1 if num1 else 0, num2 if nums2 else 0]]
            else:
                map[sum].append([num1 if num1 else 0, num2 if nums2 else 0])
    arr = sorted(map.items(), key=lambda kv: kv[1])
    print(arr)
    res = []
    for i in range(0, k):
        val = arr[i][1]
        print(val)
        for r in val:
            if len(res) == k:
                break
            res.append(r)
    return res
    # print(arr[:k])
    # print arr[:len(arr) - k]


def kSmallestPairs(self, nums1, nums2, k, heap=[]):
    for n1 in nums1:
        for n2 in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (-n1-n2, [n1, n2]))
            else:
                if heap and -heap[0][0] > n1 + n2:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-n1-n2, [n1, n2]))
                else:
                    break
    return [heapq.heappop(heap)[1] for _ in range(k) if heap]


class Solution:

    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        output = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))

        while len(output) < k and heap:

            val = heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] +
                                nums2[val[2]], val[1] + 1, val[2]))
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] +
                                nums2[val[2] + 1], val[1], val[2] + 1))
                visited.append((val[1], val[2] + 1))

        return output


kSmallestPairs([0], [2, 4, 6], 1)
