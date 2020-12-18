# Merge Intervals
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")



def merge(intervals):
    merged = []

    if len(intervals) == 0 : return merged

    for i in range(len(intervals)):
        # now, I will compare my current interval to what I already have in merged
        inteval_overpaled = False
        for m in range(len(merged)):
            # Scenario 1: there is no overlaping, if not, I will just add to the merge array.
            if intervals[i].start < merged[m].start and intervals[i].end < merged[m].end:
                continue

            # Scenario 2: the current array has a end bigger than something already stored in merge array, if so, it will be
            # join to merge. The start and end of merge could change.
            if intervals[i].start <= merged[m].end and not inteval_overpaled:
                # I need to stablish the end and of the new merge
                new_start = min(intervals[i].start, merged[m].start)
                new_end = max(intervals[i].end, merged[m].end)

                merged[m].start = new_start
                merged[m].end = new_end
                inteval_overpaled = True

        # if there is not inteval_overpaled, then I add the interval to the merged array
        if not inteval_overpaled:
            merged.append(intervals[i])

    #  this one returns the objects
    # return merged

    # this one returns the arrays
    return get_arrays(merged)


# helper function to return the interval objects as an array so can pass the tests
def get_arrays(intervals):
    arr_return = []

    for i in range(len(intervals)):
        arr_return.append([ intervals[i].start, intervals[i].end ])

    return arr_return



def main():
    print(merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
    # print("Merged intervals: ", end="")
    # for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    #     i.print_interval()
    # print()


    # print("Merged intervals: ", end='')
    # for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    #     i.print_interval()
    # print()

    # print("Merged intervals: ", end='')
    # for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    #     i.print_interval()
    # print()

main()
