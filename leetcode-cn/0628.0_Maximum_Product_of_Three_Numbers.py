'''
approach: Sort
Time: O(NlogN)
Space: O(1)

ref:
https://leetcode-cn.com/problems/maximum-product-of-three-numbers/solution/san-ge-shu-de-zui-da-cheng-ji-by-leetcod-t9sb/

执行结果：
通过
显示详情
执行用时：64 ms, 在所有 Python 提交中击败了47.30% 的用户
内存消耗：14 MB, 在所有 Python 提交中击败了27.30% 的用户
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maximum = -sys.maxint
        head = nums[0] * nums[1] * nums[2]
        mid1 = nums[0] * nums[1] * nums[-1]
        mid2 = nums[0] * nums[-2] * nums[-1]
        tail = nums[-3] * nums[-2] * nums[-1]
        maximum = max(maximum, head, mid1, mid2, tail)
        return maximum
