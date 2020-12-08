# Happy Number
# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
# square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.


# Approach using 2 pointers, a slower and faster. Based on Educative.com logic.
def find_happy_number(num):

    slower = faster = num

    # enter the cycle to search for a cycle
    # The only way to get out is by fiding a value=1 or if both pointers are the same value but now 1
    while True:
        slower = get_square_sum(slower)
        # 2 calls, so this pointer is ahead by 2. If there is a cycle, eventualy will be in the same point.
        faster = get_square_sum(get_square_sum(faster))

        if slower == faster:
            if slower == 1:
                return True
            else:
                return False



# The logic of this function is from Educative.com
def get_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        # now I will resign the value of num to only the decimal DIGIT, so in the next loop I take care of it
        num //= 10

    return _sum


def find_happy_number_v1(num):
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

