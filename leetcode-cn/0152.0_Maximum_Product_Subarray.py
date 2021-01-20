'''
approach: Dynamic Programming
Time: O(N)
Space: O(N * 2) = O(N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了78.48% 的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了22.99% 的用户

ref:
https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        maxF = [nums[0] for _ in range(size)]
        minF = [nums[0] for _ in range(size)]
        for i in range(1, size):
            maxF[i] = max(nums[i], maxF[i - 1] * nums[i], minF[i - 1] * nums[i])
            minF[i] = min(nums[i], minF[i - 1] * nums[i], maxF[i - 1] * nums[i])
        return max(maxF)
