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

'''
try twice
T: O(N)
S: O(1)
执行用时：40 ms, 在所有 Python3 提交中击败了43.13% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了20.00% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        while i < n - 1 and nums[i] <= nums[i + 1]:
            i += 1
        if i == n - 1:
            return True
        j = i + 1
        while j < n - 1 and nums[j] <= nums[j + 1]:
            j += 1
        return j == n - 1 and nums[-1] <= nums[0]

'''
把数组看成环

执行用时：40 ms, 在所有 Python3 提交中击败了43.13% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.75% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i, x in enumerate(nums):
            if x > nums[(i + 1) % len(nums)]:
                cnt += 1
        return cnt <= 1
