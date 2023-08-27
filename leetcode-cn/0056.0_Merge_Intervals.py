'''
执行用时：48 ms, 在所有 Python3 提交中击败了37.39% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了53.58% 的用户
通过测试用例：168 / 168
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for interval in intervals:
            s, e = interval
            if not ans or s > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], e)

        return ans

'''
Python3
60 ms
20.1 MB
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start, end in intervals:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans 
        