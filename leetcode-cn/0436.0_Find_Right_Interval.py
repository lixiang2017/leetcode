'''
T: O(NlogN + NlogN)
S: O(N)

执行用时：76 ms, 在所有 Python3 提交中击败了89.05% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了96.75% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_i = [(start, i) for i, (start, end) in enumerate(intervals)]
        start_i.sort()
        ans = [-1] * n 
        for i, (start, end) in enumerate(intervals):
            idx = bisect_left(start_i, (end, 0))
            if idx != n:
                ans[i] = start_i[idx][1]
        return ans 


'''
T: O(NlogN + NlogN)
S: O(N)

执行用时：80 ms, 在所有 Python3 提交中击败了86.09% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了88.46% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_i = [(start, i) for i, (start, end) in enumerate(intervals)]
        start_i.sort()
        return [start_i[idx][1] if (idx := bisect_left(start_i, (end, 0))) != n else -1 for i, (start, end) in enumerate(intervals)]

'''
sort + sort + two pointers

执行用时：88 ms, 在所有 Python3 提交中击败了81.95% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了39.05% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts, ends = zip(*intervals)
        starts = sorted(zip(starts, range(n))) 
        ends = sorted(zip(ends, range(n)))
        ans = [-1] * n 
        j = 0
        for end, i in ends:
            while j < n and starts[j][0] < end:
                j += 1
            if j < n:
                ans[i] = starts[j][1]
            else:
                break
        return ans  


        
