'''
approach: Sliding Window
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：768 ms, 在所有 Python 提交中击败了67.67%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了81.20%的用户
'''



class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total_max = -10000 * k
        current_total = 0
        size = len(nums)
        i = 0
        while i < k:
            current_total += nums[i]
            i += 1
        total_max = max(total_max, current_total)

        while i < size:
            current_total += nums[i]
            current_total -= nums[i - k]
            total_max = max(total_max, current_total)
            i += 1

        return total_max * 1.0 / k
