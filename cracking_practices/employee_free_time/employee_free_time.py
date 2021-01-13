# Employee Free Time
# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours.
# Our goal is to determine if there is a free interval which is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.


from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def find_employee_free_time(schedule):
    result = []
    working_hours = [False] * 13
    starting_shfts = []  # so I can check for special cases
    special_case = []
    max_hour = 0

    # Fill working_hours with true for whenever is someone working on that hour.
    # traverse all the employees (i) and their shifts(j), and then, set working_hours to true for all the hours the employee
    # has assigned job.
    # Also, I will keep track of the bigest hour to latter I can search for all the gaps.
    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            if len(starting_shfts) > 0:
                if schedule[i][j].end + 1 in starting_shfts:
                    special_case.append(schedule[i][j].end)
        
            starting_shfts.append(schedule[i][j].start)

            # Fill the hours of the current shift
            for s in range(schedule[i][j].start, schedule[i][j].end + 1):
                working_hours[s] = True
                max_hour = max(max_hour, s)

    # Find gaps where all the employes are not working, in other words, where working_hours = False
    for i in range(1, max_hour):
        if not working_hours[i]:
            result.append([i - 1, i + 1])
            # result.append(i - 1)
            # result.append(i + 1)

    # check for special cases
    for i in range(len(special_case)):
        result.append([special_case[i], special_case[i] + 1])

    return result



