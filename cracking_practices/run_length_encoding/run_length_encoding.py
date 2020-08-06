# Problem Domain
# Create a function that receives a string and returns the run-length encoding of it.
# INPUT				OUTPUT
# aaabbcccca 		3a2b3c1a
# aaaaaaa 			7a
# abcd				1a1b1c1d


def run_length_encoding(string):
    # basic validation
    if not string:
        raise Exception('The string must be valid.')
        return None

    # set up variables
    counter = 0
    previous_chr = string[0]
    return_string = ''

    # traverse the string
    for i in range(0, len(string)):
        if string[i] == previous_chr:
            counter +=1
        else:
            return_string += str(counter)
            return_string += string[i]
            counter = 1  # so I don't lose the current ocurrence of the first ch
            previous_chr = string[i]

    # add the last run of the string
    return_string += str(counter)
    return_string += string[i]

    return return_string


