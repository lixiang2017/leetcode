'''
approach: Prefix Product + Suffix Product
Kadane's algorithm
Time: O(N)
Space: O(N)

Explanation:
Calculate prefix product in A.
Calculate suffix product in A.
Return the max.

ref:
https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了78.48% 的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了39.75% 的用户

'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = nums[:: -1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            digits[i] *= digits[i - 1] or 1
        return max(nums + digits)
