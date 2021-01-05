from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def find_employee_free_timeV1(schedule):
    result = []
    # just to make easier to read
    shiftA = start = employeeA = 0
    shiftB = end = employeeB = 1

    # get the gaps of each employee
    gaps = []
    for i in range(len(schedule)):
        gaps.append([schedule[i][shiftA].end, schedule[i][shiftB].start])

    # get the common gaps of both employees
    start_gap = max(gaps[employeeA][start], gaps[employeeB][start])
    end_gap = min(gaps[employeeA][end], gaps[employeeB][end])
    result.append([start_gap, end_gap])
    # result.append(end_gap)

    # validate if employeeA and employeeb have a touching gap
    if (schedule[employeeB][shiftB].end + 1) == schedule[employeeA][shiftB].start:
        result.append(
            [schedule[employeeB][shiftB].end, schedule[employeeA][shiftB].start]
        )
        # result.append(schedule[employeeB][shiftB].end)
        # result.append(schedule[employeeA][shiftB].start)

    return result


def find_employee_free_time(schedule):
    result = []
    working_hours = [False] * 13
    max_hour = 0

    # Fill working_hours with true for whenever is someone working on that hour.
    # traverse all the employees (i) and their shifts(j), and then, set working_hours to true for all the hours the employee
    # has assigned job.
    # Also, I will keep track of the bigest hour to latter I can search for all the gaps.
    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            # Fill the hours of the current shift
            for s in range(schedule[i][j].start, schedule[i][j].end + 1):
                working_hours[s] = True
                max_hour = max(max_hour, s)

    # Find gaps where all the employes are not working, in other words, where working_hours = False
    for i in range(1, max_hour):
        if not working_hours[i]:
            # result.append([i - 1, i + 1])
            result.append(i-1)
            result.append(i+1)


    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end="")
    print(find_employee_free_time(input))
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end="")
    print(find_employee_free_time(input))
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end="")
    print(find_employee_free_time(input))
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()


main()
