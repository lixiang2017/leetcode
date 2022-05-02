'''
T: O(2N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了88.99% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了26.28% 的用户
通过测试用例：285 / 285
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]


'''
双向奔赴的双指针
two pointers, inplace
T: O(N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了71.84% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了31.54% 的用户
通过测试用例：285 / 285
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 != 0:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                break 

        return nums


'''
都从左边出发的双指针
two pointers, inplace
T: O(N)
S: O(1)


执行用时：40 ms, 在所有 Python3 提交中击败了71.84% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了76.34% 的用户
通过测试用例：285 / 285
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums





