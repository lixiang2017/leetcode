'''
simulation, update `prefix sum` one the fly
T: O(N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了44.53% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了78.91% 的用户
通过测试用例：55 / 55
炫耀一下:
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        pre = 1
        for x in nums:
            pre += x 
            if pre < 1:
                start += (1 - pre)
                pre = 1
        return start 


'''
执行用时：40 ms, 在所有 Python3 提交中击败了44.53% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了71.09% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_pre = nums[0]
        pre = 0
        for x in nums:
            pre += x 
            min_pre = min(min_pre, pre)
        return 1 - min_pre if min_pre < 1 else 1 


'''
执行用时：48 ms, 在所有 Python3 提交中击败了11.72% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了42.19% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_pre = nums[0]
        pre = 0
        for x in nums:
            pre += x 
            min_pre = min(min_pre, pre)
        return max(1, 1 - min_pre)

