# Problem Domain: You have a classroom and a schedule, and want to hold as many classes there as possible.




# Function that returns the class that is the first to end, starting on certain time
def get_earlier_class(classes, starting_at = '06:00'):
    if classes == [] : return []

    earlier_ending_hr = '23:00'
    earlier_ending_class = []
    for i in range(len(classes)):
        starts_at, ends_at  = classes[i]

        if starts_at >= starting_at:
            if ends_at < earlier_ending_hr :
                earlier_ending_hr = ends_at
                earlier_ending_class = classes[i]


    return earlier_ending_class

def get_schedule(classes):
    schedule = []
    # variables just to make easier to read arrays
    class_starts, class_ends = 0, 1
    next_class_stating_at = '06:00'


    for i in range(len(classes)):
        # get the class that ends earlier, from my starting class
        my_class = get_earlier_class(classes, next_class_stating_at)
        if not my_class == []:
            next_class_stating_at = my_class[class_ends]
            schedule.append(my_class)

    return (schedule)
