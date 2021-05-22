import pytest
from cracking_practices.class_scheduling.class_scheduling import get_schedule


def test_one():
    classes = [
        ["10:00","11:00"],
        ["07:00", "08:00"],
        ["09:00", "10:00"],
        ["10:30:","11:30"],
        ["09:30", "10:30"],
        ["11:00","12:00"]]

    expected = [['07:00', '08:00'], ['09:00', '10:00'], ['10:00', '11:00'], ['11:00', '12:00']]

    actual = get_schedule(classes)

    assert actual == expected, 'Error on test_one.'



def test_two():
    classes = [
        ["10:00","11:00"],
        ["09:00", "10:00"],
        ["09:30", "10:30"],
        ["11:00","12:00"]]

    expected = [['09:00', '10:00'], ['10:00', '11:00'], ['11:00', '12:00']]

    actual = get_schedule(classes)

    assert actual == expected, 'Error on test_two.'


def test_three():
    classes = []

    expected = []

    actual = get_schedule(classes)

    assert actual == expected, 'Error on test_three.'


def test_four():
    classes = [
        ["09:30", "10:30"],
        ["09:00", "10:00"],
        ["11:00","12:00"]]

    expected = [['09:00', '10:00'], ['11:00', '12:00']]

    actual = get_schedule(classes)

    assert actual == expected, 'Error on test_four.'
