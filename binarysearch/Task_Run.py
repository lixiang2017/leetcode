'''
approach: Hash Table
Time: O(N)
Space: O(N)

Your code took 98 milliseconds — faster than 71.36% in Python
'''

class Solution:
    def solve(self, tasks, k):
        curr_time = 0
        time = dict()
        for i, task in enumerate(tasks):
            if task in time:
                if time[task] > curr_time:
                    # wait to current time
                    curr_time = time[task]
                    time[task] = curr_time + k + 1
                else:
                    # no need to wait, do it directly
                    time[task] = curr_time + k + 1
            
            else:
                # do it directly
                time[task] = curr_time + k + 1
            # time slot passed 1
            curr_time += 1

        return curr_time

