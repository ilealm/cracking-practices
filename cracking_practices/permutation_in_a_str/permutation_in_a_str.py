# Permutation in a String
# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Permutation is defined as the re-arranging of the characters of the string.

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.


# Helper function that receives a string and returns a dictionary with all the ocurrencies for each letter.
def convert_str_to_dict(string):
    return_dict = dict()

    for ch in (string): # you can list as many input dicts as you want here
        if ch in return_dict:
            return_dict[ch] += 1
        else:
            return_dict[ch]  = 1

    return return_dict


def find_permutation(string, pattern):
    if len(string) == 0 or len(pattern) == 0 : return False

    # stablish my first window
    pointer_left = 0
    pointer_right = len(pattern)

    pattern_dict = convert_str_to_dict(pattern)

    while pointer_right <= len(string) :
        window_dict = convert_str_to_dict(string[pointer_left:pointer_right])

        if pattern_dict == window_dict :
            return True

        # BC both dicts are different, I will move the window one position to right
        pointer_left += 1
        pointer_right += 1

    return False






