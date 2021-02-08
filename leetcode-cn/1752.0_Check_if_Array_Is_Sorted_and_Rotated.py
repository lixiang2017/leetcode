'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nonCount = 1
        size = len(nums)
        if size < 3: return True
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                nonCount += 1
        
        return nonCount == 1 or (nonCount == 2 and nums[0] >= nums[-1])
