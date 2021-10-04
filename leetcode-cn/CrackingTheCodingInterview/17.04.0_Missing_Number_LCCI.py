'''
执行用时：28 ms, 在所有 Python3 提交中击败了97.34% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了96.77% 的用户
通过测试用例：122 / 122
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

'''
xor 
bitwise

执行用时：52 ms, 在所有 Python3 提交中击败了23.72% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了45.54% 的用户
通过测试用例：122 / 122
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, chain(nums, range(len(nums) + 1)))


'''
xor 
bitwise

执行用时：44 ms, 在所有 Python3 提交中击败了45.92% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了49.15% 的用户
通过测试用例：122 / 122
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, iy: x ^ iy[0] ^ iy[1], enumerate(nums), len(nums))
