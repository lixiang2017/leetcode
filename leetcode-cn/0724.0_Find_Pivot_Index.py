'''
Time: O(N)
Space:O(1)

执行结果：通过
显示详情
执行用时：32 ms, 在所有 Python 提交中击败了91.82%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了47.18%的用户
'''


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        current_sum = idx = 0
        for num in nums:
            left_sum = current_sum
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return idx
            current_sum += num
            idx += 1

        return -1
        