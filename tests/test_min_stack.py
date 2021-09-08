import pytest
from cracking_practices.min_stack.min_stack import Stack


# test the push on the stack
def test_push_stack():
    stack = Stack()
    value = 50
    stack.push(value)

    expected = value

    actual = stack.top()

    assert actual == expected, 'Error on test_push_stack.'


# test is_empty
def test_is_empty_false():
    stack = Stack()
    value = 50
    stack.push(value)

    expected = False

    actual = stack.is_empty()

    assert actual == expected, 'Error on test_is_empty_false.'



# test is_empty
def test_is_empty_true():
    stack = Stack()

    expected = True

    actual = stack.is_empty()

    assert actual == expected, 'Error on test_is_empty_true.'



# test the top on the stack
def test_top_stack_not_empty():
    stack = Stack()
    value = 50
    stack.push(value)
    expected = value

    actual = stack.top()

    assert actual == expected, 'Error on test_top_stack_not_empty.'


# How to test exceptions:
# https://docs.pytest.org/en/6.2.x/assert.html
# test the top on the stack
def test_top_stack_empty():
    with pytest.raises(Exception):
        stack = Stack()
        expected = Exception("The stack is empty.")

        actual = stack.top()

        assert actual == expected, 'Error on test_top_stack_empty.'


# test the pop on the stack
# def test_pop_stack():
#     stack = Stack()
#     value = 50
#     stack.push(value)
#     expected = value

#     actual = stack.pop()

#     assert actual == expected, 'Error on test_pop_stack.'


# # test the push on the min_stack
# def test_push_stack():
#     stack = Stack()
#     value = 50
#     stack.push(value)

#     expected = value

#     actual = stack.min_top()

#     assert actual == expected, 'Error on test_push_stack.'



# # test the min
# def test_min_stack():
#     stack = Stack()
#     stack.push(50)
#     stack.push(100)
#     stack.push(10)
#     stack.push(30)

#     expected = 10

#     actual = stack.min()

#     assert actual == expected, 'Error on test_min_stack.'
