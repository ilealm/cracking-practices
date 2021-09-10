import pytest
from cracking_practices.queue_with_two_stacks.queue_with_two_stacks import Queue



# test that add 4 values, then pop the first
def test_push_then_pop_second():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()

    expected = 20

    actual = q.dequeue()

    assert actual == expected, 'Error on test_push_then_pop_second.'


# test that add 3 values, then pop those 3 values
def test_push_then_pop_all():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.dequeue()

    expected = 30

    actual = q.dequeue()

    assert actual == expected, 'Error on test_push_then_pop_all.'



# test that add 3 values, then pop those 3 values
def test_pushX3_popX2_pushX1_popX1():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.dequeue()
    q.enqueue(40)


    expected = 30

    actual = q.dequeue()

    assert actual == expected, 'Error on test_pushX3_popX2_pushX1_popX1.'
