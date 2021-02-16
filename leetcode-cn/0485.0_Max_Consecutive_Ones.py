'''
approach: DP
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：328 ms, 在所有 Python 提交中击败了32.34%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了88.89%的用户
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = current_length = 0
        for num in nums:
            if num == 1:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0

        return longest
