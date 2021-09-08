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

    expected = 10

    actual = queue.peek()

    assert actual == expected, 'Error on test_reverse.'
