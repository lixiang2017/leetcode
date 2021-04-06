'''
Time: O(N)
Space: O(1)

执行用时：16 ms, 在所有 Python 提交中击败了92.68%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了59.51%的用户
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return target in nums