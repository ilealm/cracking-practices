# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]


# APPROACH: I will get the sum of the values of a current "window" whit the values of the substring k;
# then, before moving to the next window, I will delete from sum the left pointer, add 1 to both pointers
# then add to sum the new value at the right
def average_subarrays(array, K):
    arr_result = []

    if len(array) - 1 < K:
        return arr_result

    left_pointer = 0
    # rest the value orter = 0
    right_pointer = K - 1
    sum = 0

    # get the first sum of the current window inside the array
    for i in range(left_pointer, right_pointer + 1):
        sum += array[i]

    # loop to the rest of the array until I have a window to move,
    #  moving one position to right, then substracting position left, and sum new position right
    while left_pointer <= len(array) - K:
        arr_result.append(sum / K)

        # substract the value of left, and then I move the pointers
        sum -= array[left_pointer]

        # move pointers
        left_pointer += 1
        # In order to get the last value, I need to validate I'm out of index scope
        right_pointer = (
            (right_pointer + 1)
            if (right_pointer + 1 <= len(array) - 1)
            else len(array) - 1
        )

        # add the new "window value" to the sum. Now I will have all the values of the current "window"
        sum += array[right_pointer]

    return arr_result

# this is not my code. Is from educative.com
def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result


