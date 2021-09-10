import pytest
from cracking_practices.queue_reverse_k_elements.queue_reverse_k_elements import Queue


def test_one():
    q = Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    q.push(50)
    print(q.__str__())
    q.reverse(3)

    expected = 30

    actual = q.top()

    assert actual == expected, 'Error on test_one.'
