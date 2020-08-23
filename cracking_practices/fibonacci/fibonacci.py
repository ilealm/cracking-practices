def fibonacci(which_fibonacci):
    if which_fibonacci <= 2:
        return 1

    return fibonacci(which_fibonacci-1) + fibonacci(which_fibonacci-2)



