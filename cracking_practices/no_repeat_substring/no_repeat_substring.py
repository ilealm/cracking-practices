# No Repeat Substring
# Given a string, find the length of the longest substring which has no repeating characters.
# Example 1:
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def no_repeat_substring(str):
    # have 2 variables: sub_string and max_sub_string
    # traverse all the str comparing each letter.
    # if current letter not in sub_string, add it. Else set max_sub_string, reset sub_string
    # return len(max_sub_string)
    if len(str) == 0 : return 0
    sub_string = max_sub_string = ''

    for pointer in range(len(str)):
        if str[pointer] in sub_string:
            # I found a duplicate, so I'm going to reset sub_string, but before I will store the current max_sub_string
            if len(sub_string) > len(max_sub_string) :
                max_sub_string = sub_string
            sub_string = ''

        sub_string += str[pointer]

    return len(max_sub_string)


