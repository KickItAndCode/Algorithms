# 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
       if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out.append(i)
    return out

def merge(intervals):
    res = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], i[1])
        else:
            res.append(i)
    return res


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i in intervals:
                    # if the list of merged intervals is empty
                    # or if the current interval does not overlap with the previous,
                    # simply append it.
        if not merged or merged[-1][-1] < i[0]:
            merged.append(i)
                   # otherwise, there is overlap,
                   # so we merge the current and previous intervals.
        else:
            merged[-1][-1] = max(merged[-1][-1], i[-1])
    return merged
