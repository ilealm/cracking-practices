# Maximum CPU Load
# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
# Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load



def find_max_cpu_load(jobs):
    # sort the jobs
    jobs.sort(key = lambda j:j.start)
    max_single_load = 0
    max_overlaping_load = 0
    has_overlapping = False
    this_overlaping_load = 0


    for i in range(len(jobs)):
        # check if the next jobs are overlaping
        this_overlaping_load = jobs[i].cpu_load
        for j in range(i+1, len(jobs)):
            if jobs[j].start < jobs[i].end:
                # I have an overlaping, so I will use a flag to know which value returns
                has_overlapping = True
                this_overlaping_load += jobs[j].cpu_load
            else:
                break

        max_overlaping_load = max(max_overlaping_load, this_overlaping_load)
        max_single_load = max(max_single_load, jobs[i].cpu_load)


    if has_overlapping:
        return max_overlaping_load
    else:
        return max_single_load
