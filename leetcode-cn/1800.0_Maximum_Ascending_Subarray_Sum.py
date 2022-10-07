'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.16% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.00% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = pre = total = 0
        for x in nums:
            if x > pre:
                total += x 
            else:
                total = x 
            ans = max(ans, total)
            pre = x 
        return ans 
        