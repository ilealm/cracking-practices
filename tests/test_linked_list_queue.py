import pytest
from cracking_practices.linked_list_queue.linked_list_queue import Queue


def test_enqueue_x3():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    expected = q.peek()

    actual = 10

    assert actual == expected, 'Error on test_enqueue_x3.'


def test_dequeue_all():
    with pytest.raises(Exception):
        q = Queue()
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.deqeue()
        q.deqeue()
        q.deqeue()

        expected = Exception("The queue is empty.")

        actual = q.peek()

        assert actual == expected, 'Error on test_dequeue_all.'


def test_enqueue_x3_dequeue_x2_enqueue_x1():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.deqeue()
    q.deqeue()
    q.enqueue(40)
    expected = q.peek()

    actual = 30

    assert actual == expected, 'Error on test_enqueue_x2_dequeue_x2_enqueue_x1.'
