import pytest
from cracking_practices.queue_reverse.queue_reverse import Stack, Queue


def test_reverse():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)
    queue.push(50)
    queue.reverse()

    expected = 50

    actual = queue.top()

    assert actual == expected, 'Error on test_reverse.'



def test_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()

        expected = Exception("The stack is empty.")

        actual = queue.top()

        assert actual == expected, 'Error on test_empty_queue.'


def test_one_element():
    queue = Queue()
    queue.push(10)
    queue.reverse()

    expected = 10

    actual = queue.top()

    assert actual == expected, 'Error on test_one_element.'


def test_two_elements():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.reverse()

    expected = 20

    actual = queue.top()

    assert actual == expected, 'Error on test_two_elements.'



def test_three_elements():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.reverse()

    expected = 30

    actual = queue.top()

    assert actual == expected, 'Error on test_three_elements.'



def test_top():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)

    expected = 10

    actual = queue.top()

    assert actual == expected, 'Error on test_top.'
