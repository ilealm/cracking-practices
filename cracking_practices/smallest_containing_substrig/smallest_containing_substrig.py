# Smallest Window containing Substring
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# String = "aabdec"
# Pattern = "abc"
# expected = "abdec"



def find_substring(str, pattern):
    smallest = str
    #  create a set of the pattern, which I will check if exist inside my current window
    pattern_set = set(pattern)

    pointer_left = 0
    pointer_right = len(str)

    # I'm going to shrik my window from str to the inner characters
    while pointer_left < pointer_right:
        window_set = set(str[pointer_left:pointer_right])

        if pattern_set.issubset(window_set):

            if len(window_set) < len(smallest):
                smallest = str[pointer_left:pointer_right]


            if pattern in str[pointer_left:pointer_right]:
                smallest = pattern

        pointer_left += 1

    if smallest == str:
        return ""
    else:
        return smallest


