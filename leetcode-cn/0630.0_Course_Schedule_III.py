'''
heapq

执行用时：104 ms, 在所有 Python3 提交中击败了95.72% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了12.83% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq, t = [], 0
        for duration, lastDay in sorted(courses, key=lambda x: x[1]):
            if t + duration > lastDay and pq and -pq[0] > duration:
                t += heappop(pq)
            if t + duration <= lastDay:
                heappush(pq, -duration)
                t += duration

        return len(pq)
