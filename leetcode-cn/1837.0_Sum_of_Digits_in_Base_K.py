'''
执行用时：40 ms, 在所有 Python3 提交中击败了25.76% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了90.83% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            ans += n % k
            n //= k
        return ans 
        