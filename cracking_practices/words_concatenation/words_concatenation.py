# String = "catfoxcat"
# Words = ["cat", "fox"]


def get_num_ch(array):
    num_ch = 0

    for i in range(len(array)):
        num_ch += len(array[i])

    return num_ch




def find_word_concatenation(str, words):
    result_indices = []

    pointer_left = 0
    # obtain the number of characters in all the array words
    num_ch_in_words = get_num_ch(words)

    for pointer_right in range(len(str)):
        # I have to say pointer_right +1 so I can INCLUDE that chr (which is the current)
        if len(str[pointer_left:pointer_right+1]) == num_ch_in_words:
            all_words_in_window = True
            # ckech if all the words in the array exist in the current window
            for w in words:
                if not w in str[pointer_left:pointer_right+1] :
                    all_words_in_window = False

            # if all the words exist in the window, append pointer left to result_indices
            if all_words_in_window:
                result_indices.append(pointer_left)

            # regardless if the words are in the array, I shirnk the window 1 possition
            pointer_left += 1


    return result_indices


