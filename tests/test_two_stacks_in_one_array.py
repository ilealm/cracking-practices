import pytest
from cracking_practices.two_stacks_in_one_array.two_stacks_in_one_array import Stack



def test_is_empty_false():
    my_stack = Stack()
    my_stack.push1('a')

    expected = False

    actual = my_stack.is_stack_full()

    assert actual == expected, 'Error on test_is_empty_false.'



def test_is_empty_true():
    my_stack = Stack()
    my_stack.push1('a')
    my_stack.push1('a')
    my_stack.push1('a')
    my_stack.push1('a')
    my_stack.push1('a')
    my_stack.push1('a')
    my_stack.push2('a')
    my_stack.push2('a')
    my_stack.push2('a')
    my_stack.push2('a')

    expected = True

    actual = my_stack.is_stack_full()

    assert actual == expected, 'Error on test_is_empty_true.'


def test_push1():
    my_stack = Stack()
    my_stack.push1('a')

    expected = 'a'

    actual = my_stack.pop1()

    assert actual == expected, 'Error on test_push1.'




def test_push1_three_items():
    my_stack = Stack()
    my_stack.push1('a')
    my_stack.push1('b')
    my_stack.push1('c')

    expected = ['a', 'b', 'c', None, None, None, None, None, None, None]

    actual = my_stack.pop1()

    assert actual == expected, 'Error on test_push1_three_items.'


def test_push2():
    my_stack = Stack()
    my_stack.push2('1')

    expected = '1'

    actual = my_stack.pop2()
    assert actual == expected, 'Error on test_push2.'



