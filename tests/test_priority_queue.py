from _pytest.config import ExitCode
import pytest
from cracking_practices.priority_queue.priority_queue import PriorityQueue


def test_add_3():
    q = PriorityQueue()
    q.add(20)
    q.add(40)
    q.add(10)

    expected = 10

    actual = q.peek()


    assert actual == expected, 'Error on test_add_3'


def test_add_full():
    with pytest.raises(Exception):
        q = PriorityQueue()
        q.add(20)
        q.add(40)
        q.add(30)
        q.add(60)
        q.add(10)

        expected = Exception('The queue is full.')

        actual = q.add(100)


        assert actual == expected, 'Error on test_add_full'


def test_remove_empty():
    with pytest.raises(Exception):
        q = PriorityQueue()

        expected = Exception('The queue is empty.')

        actual = q.remove()

        assert actual == expected, 'Error on test_remove_empty'




def test_add_3_remove_1():
    q = PriorityQueue()
    q.add(20)
    q.add(40)
    q.add(10)

    expected = 40

    actual = q.remove()

    assert actual == expected, 'Error on test_add_3_remove_1'





def test_add_3_remove_1_add_2():
    q = PriorityQueue()
    q.add(20)
    q.add(40)
    q.add(10)
    q.remove()
    q.add(50)
    q.add(5)

    expected = 5

    actual = q.peek()

    assert actual == expected, 'Error on test_add_3_remove_1_add_2'


