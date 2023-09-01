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

'''
Python3
40 ms
18.2 MB
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = bisect_right(intervals, newInterval)
        l, r = i - 1, i
        a, b = newInterval
        while l >= 0 and intervals[l][1] >= a:
            l -= 1
        while r < n and intervals[r][0] <= b:
            r += 1
        # l + 1 -> r - 1
        left = min(a, intervals[l + 1][0] if 0 <= l + 1 < n else inf)
        right = max(b, intervals[r - 1][1] if 0 <= r - 1 < n else -inf)
        return intervals[: l + 1] + [[left, right]] + intervals[r: ]



'''
Python3
52 ms
18.2 MB

if + while
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = bisect_right(intervals, newInterval)
        a, b = newInterval
        l, r = i - 1, i
        if l >= 0 and intervals[l][1] >= a:
            l -= 1
        while r < n and intervals[r][0] <= b:
            r += 1
        # l + 1 -> r - 1
        left = min(a, intervals[l + 1][0] if 0 <= l + 1 < n else inf)
        right = max(b, intervals[r - 1][1] if 0 <= r - 1 < n else -inf)
        return intervals[: l + 1] + [[left, right]] + intervals[r: ]


