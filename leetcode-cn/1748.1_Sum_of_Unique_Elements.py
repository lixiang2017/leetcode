'''
approach: Hash Table
Time: O(N)
Space: O(N)

执行结果：通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了85.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了90.00%的用户
'''


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = defaultdict(int)
        unique = 0
        for num in nums:
            seen[num] += 1
            if seen[num] == 1:
                unique += num
            if seen[num] == 2:
                unique -= num
            
        return unique
        