# Calendar Matching
# Imagine that you want to schedule a meeting of a certain duration with a coworker. You have access to your calendar and your coworker's calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime]), as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of[earliestTime, latestTime]). Write a function that takes in your calendar, your daily bounds, your coworker's calendar, your coworker's daily bounds, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks(in the form of[startTime, endTime]) during which you could schedule the meeting. Note that times will be given and should be returned in military time(example times: '8:30', '9:01', '23:56').

from nose.tools import *


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    res = []
    # update calendars with start and end bounds
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)

    # Then merge the two arrays in a merge sort fashion
    # loop through both arrays and move pointers to the next one in line and the compare the two
    mergedCalendars = mergeCalendars(updatedCalendar1, updatedCalendar2)
    # ones merged the times will have overlapse so we want to flatten them so there are no over laping times. this will make find empty blocks easier
    flattenedCalendar = flattenCalendar(mergedCalendars)
    # loop through and look at the end time of one meeting with the start time of the next meeting
    # if the difference is >= to the meeting duration added it to the result
    # return result
    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)


def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ['0:00', dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], '23:59'])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))


def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    # merge
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    # cleanup because one can be longer than the other
    while i < len(calendar1):
        merged.append(meeting1)
        i += 1
    while j < len(calendar2):
        merged.append(meeting2)
        j += 1

    return merged


def flattenCalendar(calendar):
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        currMeeting = calendar[i]
        prevMeeting = flattened[-1]

        currStart, currEnd = currMeeting
        prevStart, prevEnd = prevMeeting

        # if this is true we know it overlaps
        if prevEnd >= currStart:
            newPrevMeeting = [prevStart, max(currEnd, prevEnd)]
            flattened[-1] = newPrevMeeting

        # no overlap so append curr meeting
        else:
            flattened.append(currMeeting[:])

    return flattened


def getMatchingAvailabilities(calendar, meetingDuration):
    matchingAvailabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        availabilityDuration = end - start
        if availabilityDuration >= meetingDuration:
            matchingAvailabilities.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))


def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes


def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursString = str(hours)
    minsString = '0' + str(mins) if mins < 10 else str(mins)
    return hoursString + ':' + minsString


calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"],
]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30
expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
result = calendarMatching(
    calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
)
print("All cases pass" if assert_equal(result, expected) == None else "Fail")


# import program
# import unittest

# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
#         dailyBounds1 = ["9:00", "20:00"]
#         calendar2 = [
#             ["10:00", "11:30"],
#             ["12:30", "14:30"],
#             ["14:30", "15:00"],
#             ["16:00", "17:00"],
#         ]
#         dailyBounds2 = ["10:00", "18:30"]
#         meetingDuration = 30
#         expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_2(self):
#         calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
#         dailyBounds1 = ["9:00", "20:00"]
#         calendar2 = [
#             ["10:00", "11:30"],
#             ["12:30", "14:30"],
#             ["14:30", "15:00"],
#             ["16:00", "17:00"],
#         ]
#         dailyBounds2 = ["10:00", "18:30"]
#         meetingDuration = 45
#         expected = [["15:00", "16:00"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_3(self):
#         calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
#         dailyBounds1 = ["8:00", "20:00"]
#         calendar2 = [
#             ["10:00", "11:30"],
#             ["12:30", "14:30"],
#             ["14:30", "15:00"],
#             ["16:00", "17:00"],
#         ]
#         dailyBounds2 = ["7:00", "18:30"]
#         meetingDuration = 45
#         expected = [["8:00", "9:00"], ["15:00", "16:00"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_4(self):
#         calendar1 = [
#             ["8:00", "10:30"],
#             ["11:30", "13:00"],
#             ["14:00", "16:00"],
#             ["16:00", "18:00"],
#         ]
#         dailyBounds1 = ["8:00", "18:00"]
#         calendar2 = [
#             ["10:00", "11:30"],
#             ["12:30", "14:30"],
#             ["14:30", "15:00"],
#             ["16:00", "17:00"],
#         ]
#         dailyBounds2 = ["7:00", "18:30"]
#         meetingDuration = 15
#         expected = []
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_5(self):
#         calendar1 = [
#             ["10:00", "10:30"],
#             ["10:45", "11:15"],
#             ["11:30", "13:00"],
#             ["14:15", "16:00"],
#             ["16:00", "18:00"],
#         ]
#         dailyBounds1 = ["9:30", "20:00"]
#         calendar2 = [
#             ["10:00", "11:00"],
#             ["12:30", "13:30"],
#             ["14:30", "15:00"],
#             ["16:00", "17:00"],
#         ]
#         dailyBounds2 = ["9:00", "18:30"]
#         meetingDuration = 15
#         expected = [
#             ["9:30", "10:00"],
#             ["11:15", "11:30"],
#             ["13:30", "14:15"],
#             ["18:00", "18:30"],
#         ]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_6(self):
#         calendar1 = [
#             ["10:00", "10:30"],
#             ["10:45", "11:15"],
#             ["11:30", "13:00"],
#             ["14:15", "16:00"],
#             ["16:00", "18:00"],
#         ]
#         dailyBounds1 = ["9:30", "20:00"]
#         calendar2 = [["10:00", "11:00"], ["10:30", "20:30"]]
#         dailyBounds2 = ["9:00", "22:30"]
#         meetingDuration = 60
#         expected = []
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_7(self):
#         calendar1 = [
#             ["10:00", "10:30"],
#             ["10:45", "11:15"],
#             ["11:30", "13:00"],
#             ["14:15", "16:00"],
#             ["16:00", "18:00"],
#         ]
#         dailyBounds1 = ["9:30", "20:00"]
#         calendar2 = [["10:00", "11:00"], ["10:30", "16:30"]]
#         dailyBounds2 = ["9:00", "22:30"]
#         meetingDuration = 60
#         expected = [["18:00", "20:00"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_8(self):
#         calendar1 = []
#         dailyBounds1 = ["9:30", "20:00"]
#         calendar2 = []
#         dailyBounds2 = ["9:00", "16:30"]
#         meetingDuration = 60
#         expected = [["9:30", "16:30"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_9(self):
#         calendar1 = []
#         dailyBounds1 = ["9:00", "16:30"]
#         calendar2 = []
#         dailyBounds2 = ["9:30", "20:00"]
#         meetingDuration = 60
#         expected = [["9:30", "16:30"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_10(self):
#         calendar1 = []
#         dailyBounds1 = ["9:30", "16:30"]
#         calendar2 = []
#         dailyBounds2 = ["9:30", "16:30"]
#         meetingDuration = 60
#         expected = [["9:30", "16:30"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)

#     def test_case_11(self):
#         calendar1 = [
#             ["7:00", "7:45"],
#             ["8:15", "8:30"],
#             ["9:00", "10:30"],
#             ["12:00", "14:00"],
#             ["14:00", "15:00"],
#             ["15:15", "15:30"],
#             ["16:30", "18:30"],
#             ["20:00", "21:00"],
#         ]
#         dailyBounds1 = ["6:30", "22:00"]
#         calendar2 = [
#             ["9:00", "10:00"],
#             ["11:15", "11:30"],
#             ["11:45", "17:00"],
#             ["17:30", "19:00"],
#             ["20:00", "22:15"],
#         ]
#         dailyBounds2 = ["8:00", "22:30"]
#         meetingDuration = 30
#         expected = [["8:30", "9:00"], ["10:30", "11:15"], ["19:00", "20:00"]]
#         result = program.calendarMatching(
#             calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
#         )
#         self.assertEqual(result, expected)


# if __name__ == "__main__":
#     unittest.main()
