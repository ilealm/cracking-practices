# Happy Number
# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
# square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def find_happy_number(num):
    sums_listed = []
    num = str(num)

    current_sum = 0
    while not current_sum == 1:
        # obtain the sum of all the digits in the current number
        for i in range(len(num)):
            current_digit = int(num[i])
            current_sum += current_digit * current_digit

        if current_sum == 1:
            return True

        # store the current sum
        if not current_sum in sums_listed:
            sums_listed.append(current_sum)
            # establish the new number to compare
            num = str(current_sum)
            current_sum = 0
        else:
            # if I already got this number, means it will never be 1
            return False

    return True

