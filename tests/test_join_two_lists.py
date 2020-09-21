from cracking_practices.join_two_lists.join_two_lists import join_two_lists

def test_one():
    lst1 = [10,15, 20,25,30]
    lst2 = [1,3,5]

    expected = [1, 3, 5, 10, 15, 20, 25, 30]

    actual = join_two_lists(lst1, lst2)

    assert actual == expected, 'Error on test_one.'


def test_two():
    lst1 = [1,7,20]
    lst2 = [5,7,25]

    expected = [1,5,7,7,20,25]

    actual = join_two_lists(lst1, lst2)

    assert actual == expected, 'Error on test_two'


def test_three():
    lst1 = []
    lst2 = [5,7,25]

    expected = []

    actual = join_two_lists(lst1, lst2)

    assert actual == expected, 'Error on test_three'


def test_four():
    lst1 = [10,15,20,25,30]
    lst2 = [5,7,17]

    expected = [5,7,10,15, 17,20,25,30]

    actual = join_two_lists(lst1, lst2)

    assert actual == expected, 'Error on test_four'
