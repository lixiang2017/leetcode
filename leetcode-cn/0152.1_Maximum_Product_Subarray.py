'''
approach: Dynamic Programming
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了92.59% 的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了74.15% 的用户

ref:
https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxF = minF = maximum = nums[0]
        isFirst = True
        for num in nums:
            if isFirst:
                isFirst = False
                continue
            mx, mn = maxF, minF
            maxF = max(num, mx * num, mn * num)
            minF = min(num, mn * num, mx * num)
            maximum = max(maximum, maxF)
        return maximum
