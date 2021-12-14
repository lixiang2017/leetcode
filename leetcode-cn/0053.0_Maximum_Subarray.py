'''
T: O(N)
S: O(1)

执行用时：100 ms, 在所有 Python3 提交中击败了76.84% 的用户
内存消耗：25.2 MB, 在所有 Python3 提交中击败了69.19% 的用户
通过测试用例：209 / 209
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for x in nums:
            if pre >= 0:
                pre += x
            else:
                pre = x
            ans = max(ans, pre)
        return ans
