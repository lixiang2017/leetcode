'''
approach: Hash Table
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了85.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了85.00%的用户
'''


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        unique = 0
        for key, val in count.iteritems():
            if 1 == val:
                unique += key
        return unique



'''
approach: Hash Table / Set
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了60.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了90.00%的用户
'''

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        ignored = set()
        unique = 0
        for num in nums:
            if num in ignored:
                continue
            if num in seen:
                unique -= num
                ignored.add(num)
            if num not in seen:
                unique += num
                seen.add(num)
        return unique
        