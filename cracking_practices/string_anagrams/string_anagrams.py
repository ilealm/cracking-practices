# String Anagrams
# Given a string and a pattern, find all anagrams of the pattern in the given string.


# Helper function that receives a string and returns a dictionary with all the ocurrencies for each letter.
def convert_str_to_dict(string):
    return_dict = dict()

    for ch in (string): # you can list as many input dicts as you want here
        if ch in return_dict:
            return_dict[ch] += 1
        else:
            return_dict[ch]  = 1

    return return_dict


def find_string_anagrams(str, pattern):
    arr_return = []
    if len(str) == 0 or len(pattern) == 0 : return arr_return

    pointer_left = 0
    pointer_right = len(pattern)

    pattern_dict = convert_str_to_dict(pattern)

    while pointer_right <= len(str) :
        window_dict = convert_str_to_dict(str[pointer_left:pointer_right])

        if pattern_dict == window_dict :
            arr_return.append(pointer_left)

        # BC both dicts are different, I will move the window one position to right
        pointer_left += 1
        pointer_right += 1

    return arr_return
