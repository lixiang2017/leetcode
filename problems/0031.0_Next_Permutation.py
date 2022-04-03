'''
two pointers
T: O(2N)
S: O(1)

Runtime: 66 ms, faster than 37.56% of Python3 online submissions for Next Permutation.
Memory Usage: 13.9 MB, less than 79.00% of Python3 online submissions for Next Permutation.
'''
'''
4 2 1 6 8 [4] 7 6 5 4 3 1
            7 7 6 5 4 3 1
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums[:] = nums[:: -1]
            return 
        
        # to find 5 pos
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # swap nums[i], nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        # reverse from i+1 to n-1
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
