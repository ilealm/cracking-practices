# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.
# String="aabccbb"
# k = 2

# expected = 'bbbbb'


def longest_subsrt_w_replacement(str, k):
    pointer_left = 0
    replacements = 0
    max_str = ''

    for pointer_right in range(1, len(str)):
        if not str[pointer_right] == str[pointer_left] :
            # If I still have replacements available, I will count one more
            if replacements < k:
                replacements += 1
            else:
                # save max
                if len(str[pointer_left:pointer_right]) > len(max_str):
                    max_str = str[pointer_left:pointer_right]

                # I reached k replacements, so I need to shrink the window to the begining of the replacements
                pointer_left += 1
                inner_runner = pointer_left + 1
                replacements = 0
                while inner_runner <= pointer_right:
                    if not str[pointer_left] == str[inner_runner]:
                        if replacements < k:
                            replacements += 1
                        else:
                            if len(str[pointer_left:pointer_right+1]) > len(max_str):
                                max_str = str[pointer_left:pointer_right]
                            pointer_left += 1

                    inner_runner += 1


    if len(str[pointer_left:pointer_right+1]) > len(max_str):
        max_str = str[pointer_left:pointer_right+1]

    return len(max_str)



