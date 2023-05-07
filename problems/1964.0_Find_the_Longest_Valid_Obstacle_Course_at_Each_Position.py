'''
Runtime: 1441 ms, faster than 100.00% of Python3 online submissions for Find the Longest Valid Obstacle Course at Each Position.
Memory Usage: 33.7 MB, less than 15.15% of Python3 online submissions for Find the Longest Valid Obstacle Course at Each Position.
'''
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        q = []
        ans = []
        for o in obstacles:
            if not q or q[-1] <= o:
                q.append(o)
                ans.append(len(q))
            else:
                i = bisect_right(q, o)
                q[i] = o
                ans.append(i + 1)
        return ans
        