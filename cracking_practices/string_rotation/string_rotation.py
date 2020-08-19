# PROBLEM DOMAIN
# String Rotation 1.9 : Assume you have a method isSubstring which checks if one word is a substring of another.(I'm not ussing this)
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstrig.
# s1 = waterbottle
# s2 = erbottlewat


# Approach 1, Traverse s2 until I find the start of s1, concatenate the rest of the letters, then check is they are the same word.
def string_rotation(original_str,lookup_str):
    if len(original_str)==0 or len(lookup_str) == 0 : return False
    if not len(original_str) == len(lookup_str) : return False
    original_str = original_str.lower()
    lookup_str = lookup_str.lower()

    for i in range(0,len(lookup_str)-1):
        if lookup_str[i] == original_str[0]:
            if original_str == lookup_str[i:] + lookup_str[0:i]:
                return True

    return False



