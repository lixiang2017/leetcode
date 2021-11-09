'''
执行用时：60 ms, 在所有 Python3 提交中击败了81.56% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了79.79% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        pre = -1
        for t in timeSeries:
            if pre < 0:
                pre = t + duration - 1
                ans += duration
            elif t > pre:
                pre = t + duration - 1
                ans += duration
            else:
                ans += t - pre + duration - 1
                pre = t + duration - 1
        return ans
        