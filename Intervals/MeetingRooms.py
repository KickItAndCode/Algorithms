# Given an array of meeting time intervals consisting of start and end times [[s1,e1], [s2,e2], ...] determine if a person could attend all meetings

# Example 1
# input [[0,30], [5,10], [15,20]]
# false


# Example 2
# input [[7,10] , [2,4]]
# true

def canAttendMeetings(intervals):
    starts = [0] * len(intervals)
    ends = [0] * len(intervals)

    for i in range(len(intervals)):
        starts[i] = intervals[i][0]
        ends[i] = intervals[i][1]

    starts.sort()
    ends.sort()

    for i in range(len(starts) - 1):
        if starts[i + 1] < ends[i]:
            return False
    return True


print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # false
print(canAttendMeetings([[7, 10], [2, 4]]))  # true
