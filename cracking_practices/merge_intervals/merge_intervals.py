from __future__ import print_function
# import math

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals):
    merged = []

    if len(intervals) == 0 : return merged

    # I always add the first interval to the merged list
    # merged.append(intervals[0])

    # for i in range(1, len(intervals)):
    for i in range(len(intervals)):
        # now, I will compare my current interval to what I already have in merged
        inteval_overpaled = False
        for m in range(len(merged)):
            # if there is an overlaping, I will merge
            if intervals[i].start <= merged[m].end and not inteval_overpaled:
                # I need to stablish the end of the new merge
                new_end = max(intervals[i].end, merged[m].end)
                merged[m].end = new_end
                inteval_overpaled = True

        # if there is not inteval_overpaled, then I add the interval to the merged array
        if not inteval_overpaled:
            merged.append(intervals[i])

    return merged


def main():
    # print(merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()


  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

#   print("Merged intervals: ", end='')
#   for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
#     i.print_interval()
#   print()

main()
