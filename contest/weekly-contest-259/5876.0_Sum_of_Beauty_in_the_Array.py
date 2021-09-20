'''
AC
'''
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N = len(nums)
        b = 0
        premax = nums[0]
        postmin = [nums[-1]] * N
        for i in range(N - 2, -1, -1):
            postmin[i] = min(postmin[i+1], nums[i + 1])
        
        for i in range(1, N - 1):
            premax = max(premax, nums[i - 1])
        
            if premax < nums[i] < postmin[i + 1]:
                b += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                b += 1
        
        return b
