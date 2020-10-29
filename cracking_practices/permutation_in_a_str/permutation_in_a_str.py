# Permutation in a String
# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Permutation is defined as the re-arranging of the characters of the string.

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

def find_permutation(string, pattern):
    if len(string) == 0 or len(pattern) == 0 : return False

    pattern_dict = dict()




    for ch in (pattern): # you can list as many input dicts as you want here
        if ch in pattern_dict:
            pattern_dict[ch] += 1
        else:
            pattern_dict[ch] = 1

        # print(d)
        # for key, value in d.items():
        #     dd[key].append(value)

    print(pattern)
    print(pattern_dict)

    # print(pattern_dict)

    # create a dictionary for the Pattern
    # create boolean variable Found and set to false
    # create pointers, left =0, right = len(pattern)
    # use a while to use sliding window method to move thought the string. this while will be until right < len(string) and not Found
    #     for each window i will tranform into a dict, then compare if both dict are equal, if so, return true
    #     move window: increase by one left and right


if __name__ == "__main__":
    print(find_permutation('bcdxabcdy', 'bcdyabcdx'))

    # add basic validations
    # create a dictionary for the Pattern
    # create boolean variable Found and set to false
    # create pointers, left =0, right = len(pattern)
    # use a while to use sliding window method to move thought the string. this while will be until right < len(string) and not Found
    #     for each window i will tranform into a dict, then compare if both dict are equal, if so, return true
    #     move window: increase by one left and right
