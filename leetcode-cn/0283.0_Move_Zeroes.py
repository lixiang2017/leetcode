'''
执行用时：36 ms, 在所有 Python3 提交中击败了99.35% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了97.48% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 1 if x != 0 else 2)


'''
执行用时：44 ms, 在所有 Python3 提交中击败了91.74% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了58.30% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # i, current not zero; j, further 
        i = j = 0
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                # nums[j] = 0  # wrong  for [1]
                i += 1
            j += 1
        
        while i < n:
            nums[i] = 0
            i += 1
