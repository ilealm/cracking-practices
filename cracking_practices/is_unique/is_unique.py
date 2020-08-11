# PROBLEM DOMAIN:
# 1.1 Is unique: Implement an algorithm to determinate if a string has all unique characters


def is_unique(string):
    if string == '':
        return False
        
    for current in range(0, len(string)-1):
        for runner in range(current+1, len(string)):
            if string[current] == string[runner]:
                return False

    return True

