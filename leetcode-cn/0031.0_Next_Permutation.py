'''
执行用时：52 ms, 在所有 Python3 提交中击败了10.69% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了83.68% 的用户
通过测试用例：265 / 265
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        21 4 18 23 36 23 1 3 3 7 7
        1 2 2 [3] 9 7 6 4 3 2 2 2 1
                        T
        '''
        n = len(nums)
        i = n - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[:: -1]
        else:
            # choose a number target nums[j] from i, i+1, ..., n-1, just larger than nums[i -1]
            j = i 
            while j < n and nums[j] > nums[i - 1]:
                j += 1
            if j == n or nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            nums[i: ] = nums[i: ][:: -1]


