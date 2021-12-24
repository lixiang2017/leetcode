'''
sort
T: O(NlogN + N)

Runtime: 84 ms, faster than 76.98% of Python3 online submissions for Merge Intervals.
Memory Usage: 16 MB, less than 97.17% of Python3 online submissions for Merge Intervals.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for inter in intervals:
            if not ans or ans[-1][1] < inter[0]:
                ans.append(inter)
            else:
                ans[-1][1] = max(ans[-1][1], inter[1])
        return ans
