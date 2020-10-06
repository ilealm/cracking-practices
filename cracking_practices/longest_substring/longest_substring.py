# Longest Substring with K Distinct Characters
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


def longest_substring(letters, K):
    window_letters = ""
    longest = 0
    window_set = set()

    for right_pointer in range(len(letters)):
        window_letters += letters[right_pointer]
        window_set.add(letters[right_pointer])

        while len(window_set) > K:
            # I need the -1 BS I just added a letter that brokes the rule of K diff. letters
            if len(window_letters) -1 > longest: # and len(window_set) <= K:
                longest = len(window_letters)-1  # or max ?

            # stablish the new set
            window_letters = window_letters[1:]
            window_set = set(window_letters)


    return longest




