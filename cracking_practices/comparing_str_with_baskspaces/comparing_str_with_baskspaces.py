# Comparing Strings containing Backspaces
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

# Example 2:
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.



# Approach not using built in functions, but using pointers
def backspace_compare_v1(str1, str2):
    pointer1 = 0
    pointer2 = 0

    #   Remove all the letters before the #, using one while
    while pointer1 < len(str1) and pointer2 < len(str2):
        if str1[pointer1] == '#':
            # remove the previous position
            str1 = str1[:pointer1-1] + str1[pointer1+1:]
        else:
            pointer1 += 1

        if str2[pointer2] == '#':
            # remove the previous position
            str2 = str2[:pointer2-1] + str2[pointer2+1:]
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


    # for pointer2
    while pointer2 < len(str2):
        if str2[pointer2] == '#':
            # remove the previous position
            str2 = str2[:pointer2-1] + str2[pointer2+1:]
            # decrease the last pointer, so I check all the spaces
            pointer2 -= 1
        else:
            pointer2 += 1


    return str1 == str2


# Using strings functions
def backspace_compare(str1, str2):

    # for str1
    bkspc = str1.find("#")
    while bkspc > 0:
        str1 = str1[:bkspc-1] + str1[bkspc +1 :]
        bkspc = str1.find("#")

    # for str2
    bkspc = str2.find("#")
    while bkspc > 0:
        str2 = str2[:bkspc-1] + str2[bkspc +1 :]
        bkspc = str2.find("#")

    return str1 == str2


