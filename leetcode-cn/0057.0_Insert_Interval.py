'''
binary search

执行用时：40 ms, 在所有 Python3 提交中击败了68.26% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了64.95% 的用户
通过测试用例：156 / 156
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect.bisect_right(intervals, newInterval)
        ans = intervals[: idx]
        for start, end in chain([newInterval], intervals[idx: ]):
            if not ans or ans[-1][-1] < start:
                ans.append([start, end])
            else:
                ans[-1][-1] = max(ans[-1][-1], end)
        return ans 

'''
bisect_left

执行用时：44 ms, 在所有 Python3 提交中击败了45.09% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了64.32% 的用户
通过测试用例：156 / 156
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect.bisect_left(intervals, newInterval)
        ans = intervals[: idx]
        for start, end in chain([newInterval], intervals[idx: ]):
            if not ans or ans[-1][-1] < start:
                ans.append([start, end])
            else:
                ans[-1][-1] = max(ans[-1][-1], end)
        return ans 