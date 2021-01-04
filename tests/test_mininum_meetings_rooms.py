import pytest
from cracking_practices.mininum_meetings_rooms.mininum_meetings_rooms import min_meeting_rooms, Meeting


def test_one():
    expected = 4

    actual = min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])

    assert actual == expected, 'Error on test_one.'



def test_two():
    expected = 2

    actual = min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])

    assert actual == expected, 'Error on test_two.'


def test_three():

    expected = 1

    actual = min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])

    assert actual == expected, 'Error on test_three.'


def test_four():

    expected = 2

    actual = min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])

    assert actual == expected, 'Error on test_four.'


