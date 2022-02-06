'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了10.00%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了5.00%的用户
'''

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        uniqueSum = 0
        for num in nums:
            if 1 == count[num]:
                uniqueSum += num
        return uniqueSum


'''
执行用时：36 ms, 在所有 Python3 提交中击败了42.04% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了87.81% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(x for x, cnt in Counter(nums).items()  if cnt == 1)
