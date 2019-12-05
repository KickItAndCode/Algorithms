
# 681. Next Closest Time

# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


def nextClosestTime(time):

    # get total current minutes by splitting the time string
    # multiply by 60 to get total time
    totalMinutes = 60 * int(time[:2]) + int(time[3:])

    # make a set of allowed characters
    allowed = {int(x) for x in time if x != ':'}
    while True:

        # add 1 to the total minutes but handle time conversion
        # to make sure its in bounds 0 <= time < 24* 60
        totalMinutes = (totalMinutes + 1) % (24 * 60)

        # calculate the next time from the total minutes as an array
        nextTime = [
            totalMinutes // 60 // 10,
            totalMinutes // 60 % 10,
            totalMinutes % 60 // 10,
            totalMinutes % 60 % 10
        ]

        # make sure each digit is inside the allowed set
        isValid = True
        for digit in nextTime:
            if not digit in allowed:
                isValid = False

        # if valid format for return
        if isValid:
            return "{:02d}:{:02d}".format(*divmod(totalMinutes, 60))


print(nextClosestTime("19:34"))  # "19:39"
print(nextClosestTime("23:59"))  # "22:22"
