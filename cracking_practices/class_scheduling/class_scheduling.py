# Problem Domain: You have a classroom, and want to hold as many classes there as possible.
# You get a list of clasess





# Function that returns the class that is the first to end, starting on certain time
def get_first_class(classes):
    if classes == [] : return []

    earlier_ending_hr = '23:00'
    earlier_ending_class = []
    for i in range(len(classes)):
        starts_at, ends_at  = classes[i]
        if ends_at < earlier_ending_hr :
            earlier_ending_hr = ends_at
            earlier_ending_class = classes[i]


    return earlier_ending_class

def get_schedule(classes):
    class_ends = get_first_class(classes)

    print(class_ends)




classes = [
    ["09:00", "10:00"],
    ["09:30", "10:30"],
    ["10:00","11:00"],
    ["10:30:","11:30"],
    ["11:00","12:00"]]
print(get_schedule(classes))


# ["07:00","08:00"],
