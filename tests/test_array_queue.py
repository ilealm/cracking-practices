import pytest
from cracking_practices.array_queue.array_queue import Queue


# push on available space
def test_push():
    queue = Queue()
    queue.push(10)
    queue.push(20)

    expected = 10

    actual = queue.peek()

    assert actual == expected, 'Error on test_push.'


# push on NOT available space. The array is size 5 in this example
# I can upd  class __init to receive the size of the array and don't have fixed size
def test_push_availabe_on_left():
    with pytest.raises(Exception):
        queue = Queue()
        queue.push(10)
        queue.push(20)
        queue.push(30)
        queue.push(40)
        queue.push(50)


        expected = Exception("The array is full.")

        actual = queue.push(60)

        assert actual == expected, 'Error on test_push_full_queue.'


# push when I have space to the left
def test_push_availabe_on_left():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)
    queue.push(50)
    queue.pop()
    queue.pop()
    queue.push(60)


    expected = 30

    actual = queue.pop()

    assert actual == expected, 'Error on test_push_availabe_on_left.'



