# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.


# minHeap fior end time
# store overlapping events in the heap

# the heap stores all overallapping events. When a new event comes, we greedily choose the vent X that finished the earliest. If the new event does not overlap with X then the new event can reuse X's room, or simply extend X's event to the envents end time

# if the new event overlaps with X, then it must overlap with all other events in the heap. So a new room must be created.

# the reason for correctnes is the invariant: heap size is always the minimum number of rooms we need so far

from heapq import *
# Time O (nLogn) | Space O(N)


def minMeetingRooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1] - x[0])

    heap = []
    heappush(heap, intervals[0])
    for i in range(1, len(intervals)):
        curr = intervals[i]
        earliest = heappop(heap)
        if curr[0] >= earliest[1]:
            earliest[1] = curr[1]
        else:
            heappush(heap, curr)

        heappush(heap, earliest)

    return len(heap)


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2)
print(minMeetingRooms([[1, 4], [5, 6], [8, 9], [2, 6],
                       [3, 6], [12, 14], [10, 13], [8, 11]]))  # 5)


def minMeetingRooms2(intervals):

    sorted(intervals, key=lambda i: i[0])
    minHeap = []
    heappush(minHeap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= minHeap[0]:
            heappop(minHeap)
        heappush(minHeap, intervals[i][1])

    return len(minHeap)


print(minMeetingRooms2([[0, 30], [5, 10], [15, 20]]))  # 2)
print(minMeetingRooms2([[1, 4], [5, 6], [8, 9], [2, 6],
                        [3, 6], [12, 14], [10, 13], [8, 11]]))  # 5)
