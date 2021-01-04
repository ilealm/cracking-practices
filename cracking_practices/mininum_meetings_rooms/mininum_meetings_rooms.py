# Minimum Meeting Rooms
# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
# mininum_meetings_rooms
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):
    rooms = 1

    # sort the list
    meetings.sort(key=lambda interval: interval.start)

    for i in range(len(meetings)-1):
        if meetings[i+1].start < meetings[i].end :
            rooms += 1

    return rooms


def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))

  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))

  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))

  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()

