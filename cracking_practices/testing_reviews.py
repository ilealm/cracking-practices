# Intervals Intersection
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.


def merge(intervals_a, intervals_b):
    result = []
    start = a = b = 0
    end = 1

    # traverse b to find intersecctions on a
    # while b < len(intervals_b):
    # for b in range(len(intervals_b)):
    while b < len(intervals_b):
        # check if not fit at all
        if intervals_b[b][start] > intervals_a[a][end]:
            a += 1
            continue

        # check if b fits in a
        if intervals_a[a][start] <= intervals_b[b][start] and intervals_b[b][end] <= intervals_a[a][end]:
            result.append(intervals_b[b])
            a += 1
            b += 1
            continue

        # check if b have interseccion with a, but b is bigger
        if intervals_a[a][start] <= intervals_b[b][start] and intervals_b[b][end] > intervals_a[a][end]:
            result.append([intervals_b[b][start], intervals_a[a][end]])

            # add the rest of the interseccion
            if a < len(intervals_a):
                intervals_b.append([intervals_a[a+1][start], intervals_b[b][end]])
                a += 1
                b += 1
                continue

    return result


def main():
#   print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
