'''
执行用时：104 ms, 在所有 Python3 提交中击败了69.61% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.37% 的用户
通过测试用例：170 / 170
'''
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans, i = 0, 1
        while n > 0:
            ans += n % i == 0
            n -= i 
            i += 1
        return ans 
        