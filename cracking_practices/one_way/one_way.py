# PROBLEM DOMAIN: One Away 1-5
# There are three types of edits that can be performed on strings: insert a character,  remove a character, or replace a character.
# Given two strings,  write a function to check if they are one edit or zero edits away. Return true or false.

# APPROACH1: Brute force, compare scenario by scenario.
def one_way(original_word, compare_word):
    # compare original_word to compare_word, if are equal, return false
    if compare_word == original_word:
        return False


    # check if there is a missing letter, in the beginning or end
    if len(compare_word) == len(original_word) -1:
        # check if the 1st letter is the only one different
        if original_word[1:] == compare_word:
            return True

        # check if the last letter is the only one different
        print(original_word[:-1])
        if original_word[:-1] == compare_word:
            return True

        # check if there is a missing letter in the middle
        for i in range(0, len(original_word)-1):
            if not original_word[i] == compare_word[i]:
                if original_word[i+1:] == compare_word[i:]:
                    return True

    # compare_word is bigger to original_word by one, if so, then check is an insert
    if len(original_word) + 1 == len(compare_word):
        for i in range(0, len(original_word)-1):
            if not original_word[i] == compare_word[i]:
                if original_word[i:] == compare_word[i+1:]:
                    return True

        # check last letter
        if original_word == compare_word[:-1]:
            return True

    # check if there is a upd letter
    if len(compare_word) == len(original_word):
        # compare each letter, if there is not equal, comprare the rest of the string
        for i in range(0, len(original_word)-1):
            if not original_word[i] == compare_word[i]:
                if original_word[i+1:] == compare_word[i+1:]:
                    return True


    return False

