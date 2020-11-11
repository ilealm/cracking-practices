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
        window = set(str[pointer_left:pointer_right])
        # print(window)
        if pattern_set.issubset(window):
            if len(window) < len(smallest):
                smallest = str[pointer_left:pointer_right]
        pointer_left += 1

    if smallest == str:
        return ""
    else:
        return smallest
