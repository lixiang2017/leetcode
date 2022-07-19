'''
simulation

Runtime: 94 ms, faster than 43.12% of Python3 online submissions for Min Max Game.
Memory Usage: 14 MB, less than 86.58% of Python3 online submissions for Min Max Game.
'''
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(0, len(nums), 2):
                x = 0 
                if i % 4 == 0:
                    x = min(nums[i], nums[i + 1])
                else:
                    x = max(nums[i], nums[i + 1])
                new_nums.append(x)
            nums = new_nums
        return nums[0]
