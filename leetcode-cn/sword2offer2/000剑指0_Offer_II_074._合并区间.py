'''
执行用时：36 ms, 在所有 Python3 提交中击败了77.78% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了89.58% 的用户
通过测试用例：168 / 168
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for interval in intervals:
            start, end = interval
            if not ans or ans[-1][1] < start:
                ans.append(interval)
            elif ans[-1][1] < end:
                ans[-1][1] = end
        return ans

'''
输入：
[[1,4],[2,3]]
输出：
[[1,3]]
预期结果：
[[1,4]]
'''

