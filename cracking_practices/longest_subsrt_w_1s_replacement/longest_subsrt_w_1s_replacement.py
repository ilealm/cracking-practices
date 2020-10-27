# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

def length_of_longest_substring(arr, k):
    replacements = 0
    max_lenght = 0
    pointer_left = 0

    for pointer_right in range(len(arr)):
        if arr[pointer_right] == 0 :
            if replacements < k :
                replacements += 1
            else :
                # save max
                max_lenght = max(max_lenght, len(arr[pointer_left : pointer_right]))
                #  I need to add one more replacement for the current pointer_right
                replacements += 1
                # now I need to shirk the window until the replacements are available again
                while replacements > k :
                    # check if the possition I'm shirinking is a replacement, if so, substract from replacements
                    if arr[pointer_left] == 0 :
                        replacements -= 1
                    # move the window 1 space
                    pointer_left += 1

    max_lenght = max(max_lenght, len(arr[pointer_left : pointer_right+1]))

    return max_lenght

