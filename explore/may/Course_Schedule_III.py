'''
approach: Sort + Greedy + Priority Queue / Heap
Time: O(NlogN)
Space: O(N)

You are here!
Your runtime beats 72.90 % of python3 submissions.
You are here!
Your memory usage beats 90.65 % of python3 submissions.
'''


import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        priority_queue = []
        day = 0
        courses.sort(key = lambda course: course[1])
        for course in courses:
            if day + course[0] <= course[1]:
                heapq.heappush(priority_queue, -course[0])
                day += course[0]
            elif priority_queue and - priority_queue[0] > course[0]:
                day += course[0] + heapq.heappop(priority_queue)    
                heapq.heappush(priority_queue, -course[0])
        
        return len(priority_queue)
        