'''
sort

执行用时：52 ms, 在所有 Python3 提交中击败了36.02% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了54.79% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for t in timePoints:
            h, m = list(map(int, t.split(':')))
            times.append(h * 60 + m)
        times.sort()
        times.append(times[0] + 24 * 60)
        ans = 12 * 60
        n = len(times)
        for i in range(1, n):
            ans = min(ans, times[i] - times[i - 1])
        return ans
