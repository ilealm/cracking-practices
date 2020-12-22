

# Insert Interval
# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and
# merge all necessary intervals to produce a list that has only mutually exclusive intervals.


def insert(intervals, new_interval):
    merged = []

    ni_start = new_interval[0]
    ni_end = new_interval[1]

    new_start = new_end = 0
    new_interval_appended = False

    for i in range(0,len(intervals)):

        # if I already appended the new interval, just append the rest of the intervals
        if new_interval_appended:
            merged.append(intervals[i])
            continue

        if ni_start > intervals[i][1]:
            # there is no overlap with interval
            merged.append(intervals[i])
            continue

        # check for overlap when the new interval is smaller than current start
        if ni_start < intervals[i][0]:
            # there is a overlaping. Obtain the new end and start
            new_start = min(ni_start, intervals[i][0])
            new_end = max(ni_end, intervals[i][1])

            # BS is an ordeded array, I need to check if the next position overlaps the current I'm goin to append
            if i < len(intervals):
                if intervals[i+1][0] <= new_end:
                    new_end = intervals[i+1][1]
                    merged.append([new_start, new_end])

                    break

            new_interval_appended = True
            merged.append([new_start, new_end])


    return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
