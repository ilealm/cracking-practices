# Conflicting Appointments
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.


def can_attend_all_appointments(intervals):
    if len(intervals) <= 0: return False
    if len(intervals) == 1: return True

    # just to make easier to read
    start = 0
    end = 1

    # First, I need to sort the intervals. This way works fine
    # intervals.sort()
    # this option, is from Educative.com
    # intervals.sort(key=lambda x: x[0])
    intervals.sort(key= lambda interval:interval[start])

    # now, I will check until len-1, if i[end] > i+1[start], if so, return False
    for i in range(len(intervals) - 1):
        if intervals[i+1][start] < intervals[i][end] :
            return False

    # if I made it to this point, means I don't have any overlapping appointments.
    return True

