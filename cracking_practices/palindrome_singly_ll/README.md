[Table of Contents](../../README.md)

# Problem Palindrome LinkedList

### PROBLEM DOMAIN
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once
the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

### VISUALS

```
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, To get the middle of the LL, and from there, i will have 2 pointers: left and right, and I will compare each other moving
# towards the outer limits

```
crea a  helper function that will return the middle node of the singly LL, with the position on the LL and a true/false flag depending on if the ll is even or not.

create a helper function that returns the k node of a LL

create a function that receives a ll head

    middle_info = get_middle_node(head)
    middle_node, middle_position, is_even = (
        middle_info[0],
        middle_info[1],
        middle_info[2],
    )

    set my pointers to start the comparing, from the middle to the edges
    left_position = middle_position - 1
    pointer_left = get_k_node(head, left_position)

    depending on if is even or not the LL, i will possition the pointers left and rigth to check against each other

    
    while pointer_right:
        if not pointer_left.value == pointer_right.value:
            return False

        left_position -= 1
        pointer_left = get_k_node(head, left_position)
        pointer_right = pointer_right.next

    return True
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the LL.

**Space O(1):** I'm not creating any new DS based on input.

### CODE

[cracking_practices/palindrome_singly_ll/palindrome_singly_ll.py](palindrome_singly_ll.py)

### TESTS

[tests/test_palindrome_singly_ll.py](../../tests/test_palindrome_singly_ll.py)

### GITHUB BRANCH

[Pull Request # 67, Branch: palindrome_singly_ll](https://github.com/ilealm/cracking-practices/pull/67)
