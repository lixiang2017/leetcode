'''
You are here!
Your runtime beats 82.36 % of python submissions.
'''


import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums
        self.array = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled_nums = []
        backup = list(self.origin)
        for i in range(len(backup)):
            pop_index = random.randrange(len(backup))
            num = backup.pop(pop_index)
            shuffled_nums.append(num)
            
        return shuffled_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()