[Table of Contents](../../README.md)

# Problem Comparing Strings containing Backspaces

<!-- [Whiteboard approach](comparing_str_with_baskspaces) -->

### PROBLEM DOMAIN
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

### VISUALS

```
Example 1:
Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Example 2:
Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, using 2 pointers

```

    Remove all the letters before the #, using one while
    while pointer1 < len(str1) and pointer2 < len(str2):
        if str1[pointer1] == '#':
            remove the previous position
        else:
            pointer1 += 1

        if str2[pointer2] == '#':
            # remove the previous position
        else:
            pointer2 += 1

    # check for remainder values that didn't pass on the last while
    # for pointer1
    while pointer1 < len(str1):
        if str1[pointer1] == '#':
            # remove the previous position
            str1 = str1[:pointer1-1] + str1[pointer1+1:]
            # decrease the last pointer, so I check all the spaces
            pointer1 -= 1
        else:
            pointer += 1


    same for for pointer2

    return str1 == str2

```

#### APPROACH 2, using build in string methods

```
    # for str1
    bkspc = str1.find("#")
    while bkspc > 0:
        str1 = str1[:bkspc-1] + str1[bkspc +1 :]
        bkspc = str1.find("#")

    same for str2

    return str1 == str2

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the strings.

**Space O(1):** I'm creating the same DS regardless the input.

### CODE

[cracking_practices/comparing_str_with_baskspaces/comparing_str_with_baskspaces.py](comparing_str_with_baskspaces.py)

### TESTS

[tests/test_comparing_str_with_baskspaces.py](../../tests/test_comparing_str_with_baskspaces.py)

### GITHUB BRANCH

[Pull Request # 59, Branch: comparing_str_with_baskspaces](https://github.com/ilealm/cracking-practices/pull/59)
